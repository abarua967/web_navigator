import os
import glob
import pandas as pd
import networkx as nx
from bs4 import BeautifulSoup
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, BitsAndBytesConfig

def parse_html(html_content):
    return BeautifulSoup(html_content, "lxml")

def extract_accessible_elements(soup):
    elements = []
    for tag in soup.find_all(True):
        role = tag.get("role")
        name = tag.name

        if name in ["a", "button", "input", "select", "textarea"]:
            elements.append((name, tag.text.strip() if tag.text else ""))
        if name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            elements.append(("heading", tag.text.strip() if tag.text else ""))
        if role in ["navigation", "main", "search"]:
            elements.append(("landmark", role))
    return elements

def build_navigation_graph(elements):
    G = nx.DiGraph()
    for i, el in enumerate(elements):
        node_id = f"n{i}"
        G.add_node(node_id, type=el[0], label=el[1])
        if i > 0:
            G.add_edge(f"n{i-1}", node_id, action="tab")
            
    for i in range(len(elements)):
        source_node = f"n{i}"
        
        for j in range(i + 1, len(elements)):
            if elements[j][0] == "heading":
                G.add_edge(source_node, f"n{j}", action="H")
                break 
                
        for j in range(i + 1, len(elements)):
            if elements[j][0] == "landmark":
                G.add_edge(source_node, f"n{j}", action="D")
                break 
    return G

def generate_dynamic_tasks(elements):
    tasks = []
    for i, el in enumerate(elements):
        if "search" in el[1].lower():
            tasks.append({"target": el[1], "target_id": f"n{i}", "description": "Reach search field"})
            return tasks
    for i, el in enumerate(elements):
        if el[0] == "landmark" and el[1].lower() == "main":
            tasks.append({"target": el[1], "target_id": f"n{i}", "description": "Reach main content area"})
            return tasks
    for i, el in enumerate(elements):
        if el[0] == "heading" and el[1].strip() != "":
            tasks.append({"target": el[1], "target_id": f"n{i}", "description": f"Reach heading: {el[1]}"})
            return tasks
    if len(elements) > 2:
        tasks.append({"target": elements[2][1], "target_id": "n2", "description": f"Reach {elements[2][1]}"})
        return tasks
    return tasks

def simulate_navigation(plan, graph):
    current = "n0" 
    steps = plan.split("\n")
    
    for step in steps:
        if "Tab" in step:
            neighbors = list(graph.successors(current))
            if neighbors:
                for neighbor in neighbors:
                    if graph.edges[current, neighbor].get("action") == "tab":
                        current = neighbor
                        break
        elif "H" in step:
            current_idx = int(current[1:])
            for i in range(current_idx + 1, len(graph.nodes)):
                if graph.nodes[f"n{i}"]["type"] == "heading":
                    current = f"n{i}"
                    break 
        elif "D" in step:
            current_idx = int(current[1:])
            for i in range(current_idx + 1, len(graph.nodes)):
                if graph.nodes[f"n{i}"]["type"] == "landmark":
                    current = f"n{i}"
                    break 
    return current

if __name__ == "__main__":
    FOLDER_PATH = './data/html_pages'
    RESULTS_FILE = './mathstral_results.csv'

    if not os.path.exists(FOLDER_PATH):
        print(f"[ERROR] Target directory '{FOLDER_PATH}' not found.")
        exit(1)

    html_files = glob.glob(os.path.join(FOLDER_PATH, "*.html"))
    print(f"[INFO] Files discovered: {len(html_files)}")

    MODEL_NAME = "mistralai/Mathstral-7B-v0.1"
    
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
    )

    print(f"[INFO] Loading {MODEL_NAME}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        quantization_config=bnb_config,
        device_map="auto",
        low_cpu_mem_usage=True,
        use_safetensors=True  
    )

    generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

    def generate_plan(prompt):
        result = generator(prompt, max_new_tokens=200, return_full_text=False)
        return result[0]["generated_text"]

    experiment_results = []

    for i, file_path in enumerate(html_files, 1):
        file_name = os.path.basename(file_path)
        print(f"\nProcessing [{i}/{len(html_files)}]: {file_name}")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                html_content = f.read()

            soup = parse_html(html_content)
            elements = extract_accessible_elements(soup)

            MAX_ELEMENTS = 400
            original_length = len(elements)
            if original_length > MAX_ELEMENTS:
                elements = elements[:MAX_ELEMENTS]

            graph = build_navigation_graph(elements)
            tasks = generate_dynamic_tasks(elements)

            if not tasks:
                print(f"[WARN] No tasks built for {file_name}. Skipping.")
                continue

            task = tasks[0]
            print(f"Target node: {task['target_id']} | {task['description']}")
            
            try:
                optimal_steps = nx.shortest_path_length(graph, source="n0", target=task["target_id"])
            except nx.NetworkXNoPath:
                optimal_steps = 1

            prompt = f"""Generate keyboard navigation instructions using ONLY 'Tab', 'H', and 'D'.
Output numbered steps.

EXAMPLE PAGE:
[('landmark', 'navigation'), ('heading', 'Welcome'), ('a', 'Login'), ('input', 'Search field')]
TARGET: 'Search field'
OUTPUT:
1. D
2. H
3. Tab
4. Tab

ACTUAL PAGE:
{elements}

TARGET: {task['target']}
OUTPUT:
"""
            plan = generate_plan(prompt)

            final_node = simulate_navigation(plan, graph)
            final_node_data = graph.nodes[final_node]
            success = 1 if task['target'].lower() in str(final_node_data).lower() else 0

            actual_steps = len([s for s in plan.split('\n') if s.strip()])
            safe_optimal = max(1, optimal_steps)
            path_optimality = (actual_steps / safe_optimal) if success else None

            status_str = "SUCCESS" if success else "FAILED"
            print(f"Result: {status_str} | Target steps: {optimal_steps} | Steps taken: {actual_steps}")
            if success:
                print(f"Optimality ratio: {path_optimality:.2f}")

            experiment_results.append({
                "model": "Mathstral 7B",
                "page": file_name,
                "element_count": original_length,
                "task": task["description"],
                "success": success,
                "optimal_steps": optimal_steps,
                "actual_steps": actual_steps,
                "path_optimality": path_optimality
            })

        except Exception as e:
            print(f"[ERROR] Exception on {file_name}: {str(e)}")
            experiment_results.append({
                "model": "Mathstral 7B",
                "page": file_name,
                "element_count": original_length if 'original_length' in locals() else 0,
                "task": "CRASHED",
                "success": 0,
                "optimal_steps": 0,
                "actual_steps": 0,
                "path_optimality": None
            })

    print(f"\n[INFO] Committing metrics to {RESULTS_FILE}...")
    df = pd.DataFrame(experiment_results)
    df.to_csv(RESULTS_FILE, index=False)
    
    successful_tasks = df[df["success"] == 1]
    if not successful_tasks.empty:
        avg_optimality = successful_tasks["path_optimality"].mean()
        print(f"Mean optimality ratio (successful instances): {avg_optimality:.2f}")
    else:
        print("[INFO] No successful paths to compute mean metrics.")
        
    print("Execution complete.")