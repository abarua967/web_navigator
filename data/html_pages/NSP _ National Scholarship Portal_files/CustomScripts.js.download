const header = document.querySelector(".page-header");
const toggleClass = "is-sticky";

window.addEventListener("scroll", () => {
  const currentScroll = window.pageYOffset;
  if (currentScroll > 100) {
    header.classList.add(toggleClass);
  } else {
    header.classList.remove(toggleClass);
  }
});







const clickx = document.getElementById('pencet');
    const offcanvas = document.querySelector('.offcanvas');
    let isOpen = false;

    clickx.addEventListener('click', function(event) {
      event.stopPropagation(); // Preventing the click event from bubbling up to the body
      isOpen = !isOpen;
      clickx.classList.toggle('Diam');
    });

    document.body.addEventListener('click', function(event) {
      if (isOpen && !offcanvas.contains(event.target)) {
        clickx.classList.remove('Diam');
        isOpen = false;
      }
    });







  
  

/********************************* */


  $(document).ready(function () {
	$("#hide").click(function () {
	  $("#annou").toggle('slow');
	});

  });


  $(document).ready(function () {
	$("#serch-btn").click(function () {
	  $("#serch-box-mob").toggle('slow');
	});

  });

  $(document).ready(function(){

	$("#step-btn-one").click(function(){
	  $("#step-one").hide();
	  $("#step-two").show();
	  $("#step-three").hide();
	  $("#step-four").hide();
	});

	$("#step-btn-two").click(function(){
		$("#step-one").hide();
		$("#step-two").hide();
		$("#step-three").show();
		$("#step-four").hide();
	  });

	  $("#step-btn-three").click(function(){
		$("#step-one").hide();
		$("#step-two").hide();
		$("#step-three").hide();
		$("#step-four").show();
	  });

	  $("#step-btn-four").click(function(){
		$("#step-one").hide();
		$("#step-two").hide();
		$("#step-three").hide();
		$("#step-four").hide();
	  });


	  $("#cancel-btn-one").click(function(){
		$("#step-one").show();
		$("#step-two").hide();
		$("#step-three").hide();
		$("#step-four").hide();
	  });

	  $("#cancel-btn-two").click(function(){
		$("#step-one").hide();
		$("#step-two").hide();
		$("#step-three").show();
		$("#step-four").hide();
		$("#AadhaarDetails").hide();
	  });

	  $("#cancel-btn-three").click(function(){
		$("#step-one").hide();
		$("#step-two").show();
		$("#step-three").hide();
		$("#step-four").hide();
	  });

	  $("#cancel-btn-four").click(function(){
		$("#step-one").hide();
		$("#step-two").hide();
		$("#step-three").show();
		$("#step-four").hide();
		$("#IhaveEID").hide();
	  });

	  $("#cancel-btn-five").click(function(){
		$("#step-one").hide();
		$("#step-two").hide();
		$("#step-three").show();
		$("#step-four").hide();
		$("#GuardianDetails").hide();
	  });



	  $("#Details-Finish").click(function(){
		$("#step-one").hide();
		$("#step-two").hide();
		$("#step-three").hide();
		$("#step-four").show();
		$("#AadhaarDetails").hide();
	  });

	  $("#GuardianFinish").click(function(){
		$("#step-one").hide();
		$("#step-two").hide();
		$("#step-three").hide();
		$("#step-four").show();
		$("#GuardianDetails").hide();
	  });

	  $("#EnterDetailsVerify").click(function(){
		$("#step-one").hide();
		$("#step-two").hide();
		$("#step-three").hide();
		$("#step-four").show();
		$("#IhaveEID").hide();
	  });

	  $("#GuardianAadhaarVerify").click(function(){
		$("#step-one").hide();
		$("#step-two").hide();
		$("#step-three").hide();
		$("#step-four").show();
	  });
	  

	
	  



  });


  $("input:radio[name='toggler']").click(function() {
	$("#group2 .hidden").hide().removeClass("shown");
	$("#" + $(this).val()).show();
	setTimeout(function() {
	  $(".hidden").addClass("shown");
	}, 0);
  });
  



  /*********  pageScroll*************/

  $(document).ready(function () {

	pageScroll();
	$("#contain").mouseover(function () {
	  clearTimeout(my_time);
	}).mouseout(function () {
	  pageScroll();
	});

  });

  var my_time;
  function pageScroll() {
	var objDiv = document.getElementById("contain");
	objDiv.scrollTop = objDiv.scrollTop + 1;
	if ((objDiv.scrollTop + 330) == objDiv.scrollHeight) {
	  objDiv.scrollTop = 0;
	}
	my_time = setTimeout('pageScroll()', 25);
  }





/*************************footer-logo******************** */


  $("#footer-logo").owlCarousel({
    items:7,
    loop:true,
	dots: false,
    autoplay:false,
    autoplayTimeout:1000,
    autoplayHoverPause:true,
	responsive: {
                  0: {
                    items: 2
                  },
                  600: {
                    items: 3
                  },
                  1000: {
                    items: 4
                  },
				  1025: {
                    items: 7
                  }
                }

});


















$(document).ready(function(){

	var current_fs, next_fs, previous_fs, completed_fs; //fieldsets
	var opacity;
	var current = 1;
	var completed= 1;
	var steps = $("fieldset").length;
	
	setProgressBar(current);
	
	$(".next").click(function(){
	
	current_fs = $(this).parent();
	next_fs = $(this).parent().next();
	
	//Add Class Active
	$("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

	
	//show the next fieldset
	next_fs.show();
	//hide the current fieldset with style
	current_fs.animate({opacity: 0}, {
	step: function(now) {
	// for making fielset appear animation
	opacity = 1 - now;
	
	current_fs.css({
	'display': 'none',
	'position': 'relative'
	});
	

	next_fs.css({'opacity': opacity});
	},
	duration: 500
	});
	setProgressBar(++current);
	});
	
	
	$(".previous").click(function(){
	
	current_fs = $(this).parent();
	previous_fs = $(this).parent().prev();
	
	//Remove class active
	$("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

	$("#progressbar li").eq($("fieldset").index(completed_fs)).removeClass("completed");





	//show the previous fieldset
	previous_fs.show();
	
	//hide the current fieldset with style
	current_fs.animate({opacity: 0}, {
	step: function(now) {
	// for making fielset appear animation
	opacity = 1 - now;
	
	current_fs.css({
	'display': 'none',
	'position': 'relative'
	});
	previous_fs.css({'opacity': opacity});
	},
	duration: 500
	});
	setProgressBar(--current);
	});
	
	function setProgressBar(curStep){
	var percent = parseFloat(100 / steps) * curStep;
	percent = percent.toFixed();
	$(".progress-bar")
	.css("width",percent+"%")
	}
	
	$(".submit").click(function(){
	return false;
	})

	//Add Class Completed


	$(".next").click(function(){
	
		completed_fs = $(this).parent();
		next_fs = $(this).parent().next();
		
		//Add Class Active
		$("#progressbar li").eq($("fieldset").index(completed_fs)).addClass("completed");
	
		
		//show the next fieldset
		next_fs.show();
		//hide the current fieldset with style
		completed_fs.animate({opacity: 0}, {
		step: function(now) {
		// for making fielset appear animation
		opacity = 1 - now;
		
		current_fs.css({
		'display': 'none',
		'position': 'relative'
		});
		
	
		completed_fs.css({'opacity': opacity});
		},
		duration: 500
		});
		setProgressBar(++completed);
		});

	
	});






// Limited Masking with Validation on Blur
Array.from(document.getElementsByClassName('limited')).forEach(e => {
	e.addEventListener('input', function() {
	  this.value = this.value.replace(/[^\d\(\)\-\s]/g, '')
	})

  })

	
	document.addEventListener('DOMContentLoaded', () => {
		const form = document.getElementById('otp-form')
		//const inputs = [...form.querySelectorAll('input[type=text]')]
		//const submit = form.querySelector('button[type=submit]')
	
		const handleKeyDown = (e) => {
			if (
				!/^[0-9]{1}$/.test(e.key)
				&& e.key !== 'Backspace'
				&& e.key !== 'Delete'
				&& e.key !== 'Tab'
				&& !e.metaKey
			) {
				e.preventDefault()
			}
	
			if (e.key === 'Delete' || e.key === 'Backspace') {
				const index = inputs.indexOf(e.target);
				if (index > 0) {
					inputs[index - 1].value = '';
					inputs[index - 1].focus();
				}
			}
		}
	
		const handleInput = (e) => {
			const { target } = e
			const index = inputs.indexOf(target)
			if (target.value) {
				if (index < inputs.length - 1) {
					inputs[index + 1].focus()
				} else {
					submit.focus()
				}
			}
		}
	
		const handleFocus = (e) => {
			e.target.select()
		}
	
		const handlePaste = (e) => {
			e.preventDefault()
			const text = e.clipboardData.getData('text')
			if (!new RegExp(`^[0-9]{${inputs.length}}$`).test(text)) {
				return
			}
			const digits = text.split('')
			inputs.forEach((input, index) => input.value = digits[index])
			submit.focus()
		}
	
//		inputs.forEach((input) => {
//			input.addEventListener('input', handleInput)
//			input.addEventListener('keydown', handleKeyDown)
//			input.addEventListener('focus', handleFocus)
//			input.addEventListener('paste', handlePaste)
//		})
	})  

	document.addEventListener('DOMContentLoaded', () => {
		const form = document.getElementById('otp-form1')
		//const inputs = [...form.querySelectorAll('input[type=text]')]
		//const submit = form.querySelector('button[type=submit]')
	
		const handleKeyDown = (e) => {
			if (
				!/^[0-9]{1}$/.test(e.key)
				&& e.key !== 'Backspace'
				&& e.key !== 'Delete'
				&& e.key !== 'Tab'
				&& !e.metaKey
			) {
				e.preventDefault()
			}
	
			if (e.key === 'Delete' || e.key === 'Backspace') {
				const index = inputs.indexOf(e.target);
				if (index > 0) {
					inputs[index - 1].value = '';
					inputs[index - 1].focus();
				}
			}
		}
	
		const handleInput = (e) => {
			const { target } = e
			const index = inputs.indexOf(target)
			if (target.value) {
				if (index < inputs.length - 1) {
					inputs[index + 1].focus()
				} else {
					submit.focus()
				}
			}
		}
	
		const handleFocus = (e) => {
			e.target.select()
		}
	
		const handlePaste = (e) => {
			e.preventDefault()
			const text = e.clipboardData.getData('text')
			if (!new RegExp(`^[0-9]{${inputs.length}}$`).test(text)) {
				return
			}
			const digits = text.split('')
			inputs.forEach((input, index) => input.value = digits[index])
			submit.focus()
		}
	
//		inputs.forEach((input) => {
//			input.addEventListener('input', handleInput)
//			input.addEventListener('keydown', handleKeyDown)
//			input.addEventListener('focus', handleFocus)
//			input.addEventListener('paste', handlePaste)
//		})
	})  

	document.addEventListener('DOMContentLoaded', () => {
		const form = document.getElementById('otp-form2')
		//const inputs = [...form.querySelectorAll('input[type=text]')]
		//const submit = form.querySelector('button[type=submit]')
	
		const handleKeyDown = (e) => {
			if (
				!/^[0-9]{1}$/.test(e.key)
				&& e.key !== 'Backspace'
				&& e.key !== 'Delete'
				&& e.key !== 'Tab'
				&& !e.metaKey
			) {
				e.preventDefault()
			}
	
			if (e.key === 'Delete' || e.key === 'Backspace') {
				const index = inputs.indexOf(e.target);
				if (index > 0) {
					inputs[index - 1].value = '';
					inputs[index - 1].focus();
				}
			}
		}
	
		const handleInput = (e) => {
			const { target } = e
			const index = inputs.indexOf(target)
			if (target.value) {
				if (index < inputs.length - 1) {
					inputs[index + 1].focus()
				} else {
					submit.focus()
				}
			}
		}
	
		const handleFocus = (e) => {
			e.target.select()
		}
	
		const handlePaste = (e) => {
			e.preventDefault()
			const text = e.clipboardData.getData('text')
			if (!new RegExp(`^[0-9]{${inputs.length}}$`).test(text)) {
				return
			}
			const digits = text.split('')
			inputs.forEach((input, index) => input.value = digits[index])
			submit.focus()
		}
	
//		inputs.forEach((input) => {
//			input.addEventListener('input', handleInput)
//			input.addEventListener('keydown', handleKeyDown)
//			input.addEventListener('focus', handleFocus)
//			input.addEventListener('paste', handlePaste)
//		})
	})  

	document.addEventListener('DOMContentLoaded', () => {
		const form = document.getElementById('otp-form3')
		//const inputs = [...form.querySelectorAll('input[type=text]')]
		//const submit = form.querySelector('button[type=submit]')
	
		const handleKeyDown = (e) => {
			if (
				!/^[0-9]{1}$/.test(e.key)
				&& e.key !== 'Backspace'
				&& e.key !== 'Delete'
				&& e.key !== 'Tab'
				&& !e.metaKey
			) {
				e.preventDefault()
			}
	
			if (e.key === 'Delete' || e.key === 'Backspace') {
				const index = inputs.indexOf(e.target);
				if (index > 0) {
					inputs[index - 1].value = '';
					inputs[index - 1].focus();
				}
			}
		}
	
		const handleInput = (e) => {
			const { target } = e
			const index = inputs.indexOf(target)
			if (target.value) {
				if (index < inputs.length - 1) {
					inputs[index + 1].focus()
				} else {
					submit.focus()
				}
			}
		}
	
		const handleFocus = (e) => {
			e.target.select()
		}
	
		const handlePaste = (e) => {
			e.preventDefault()
			const text = e.clipboardData.getData('text')
			if (!new RegExp(`^[0-9]{${inputs.length}}$`).test(text)) {
				return
			}
			const digits = text.split('')
			inputs.forEach((input, index) => input.value = digits[index])
			submit.focus()
		}
	
//		inputs.forEach((input) => {
//			input.addEventListener('input', handleInput)
//			input.addEventListener('keydown', handleKeyDown)
//			input.addEventListener('focus', handleFocus)
//			input.addEventListener('paste', handlePaste)
//		})
	})  

	

	$(document).ready(function(){
		$("#I-Agree").click(function(){
		 $("#AadhaarDetails").show();
		 $("#step-three").hide();
	

		});
		$("#IhaveVerifyEID").click(function(){
			$("#IhaveEID").show();
			$("#step-three").hide();
	
  
		  });

		  $("#I-Agree1").click(function(){
			$("#GuardianDetails").show();
			$("#step-three").hide();
	
  
		  });
		
	
	  });
	
