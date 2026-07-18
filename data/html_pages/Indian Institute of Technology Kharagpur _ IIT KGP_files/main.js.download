$(function () {  
    //increases font size when "+" is clicked
    var desktop1920 = 62.5;
    var desktop1600 = 58;
    var tab1024 = 54;
    var mobile = 48;
    var  count = 0;
    $(".inc").click(function() {
            if(count < 5){
                if($(window).width() > 1600){
                    var fz = desktop1920 += 1;
                    $('html').css('font-size' , fz + '%')
                } else  if($(window).width() >= 1025){
                    var fz = desktop1600 += 1;
                    $('html').css('font-size' , fz + '%')
                } else if($(window).width() >= 767){
                    var fz = tab1024 += 1;
                    $('html').css('font-size' , fz + '%')
                }else if($(window).width() > 0){
                    var fz = mobile += 1;
                    $('html').css('font-size' , fz + '%')
                }
                count++
            }
    });
    $(".dec").click(function() {
        if(count > -5){
            if($(window).width() > 1600){
                var fz = desktop1920 -= 1;
                $('html').css('font-size' , fz + '%')
            } else  if($(window).width() >= 1025){
                var fz = desktop1600 -= 1;
                $('html').css('font-size' , fz + '%')
            } else if($(window).width() >= 767){
                var fz = tab1024 -= 1;
                $('html').css('font-size' , fz + '%')
            }else if($(window).width() > 0){
                var fz = mobile -= 1;
                $('html').css('font-size' , fz + '%')
            }
            count--
        }
    });
    $('.fontSize').click(function () {  
        if($(window).width() > 1600){
            var fz = 62.5;
            $('html').css('font-size' , fz + '%')
        } else  if($(window).width() >= 1025){
            var fz = 58;
            $('html').css('font-size' , fz + '%')
        } else if($(window).width() >= 767){
            var fz = 54;
            $('html').css('font-size' , fz + '%')
        }else if($(window).width() > 0){
            var fz =48;
            $('html').css('font-size' , fz + '%')
        }
        count = 0
    })
    $('[data-toggle="tooltip"]').tooltip({
        placement:'bottom'
    });   

    //   Scroll Animation Content
    new WOW({
        boxClass:     'wow',      // animated element css class (default is wow)
        animateClass: 'animated', // animation css class (default is animated)
        offset:       0,          // distance to the element when triggering the animation (default is 0)
        mobile:       true,       // trigger animations on mobile devices (default is true)
        live:         true,       // act on asynchronously loaded content (default is true)
        callback:     function(box) {},
        scrollContainer: null,    // optional scroll container selector, otherwise use window,
        resetAnimation: true,     // reset animation on end (default is true)
        }
    ).init();

    $('.logo-menu nav ul ul').parent('li').append('<span class="subMenu"><i class="far fa-angle-down"></i></span>')
    $('.header-active').parent('main').children('header').addClass('active')
    $('.mega-menu').parent('li').addClass('has-mega-menu').children('a').attr('href' ,'javascript:Void()')
        $('.has-mega-menu a').click(function () {  
            $(this).next('.mega-menu').slideToggle();
            $('.mega-menu').not( $(this).next('.mega-menu')).slideUp()
           
        })
    var mouseMove = 0
    $('main').mousemove( function (e) {  
        if(mouseMove < e.clientX){
            $('.primary-menu-links li a ,  .logo-menu nav ul li a').removeClass('cursor')
        }else{
            $('.primary-menu-links li a ,  .logo-menu nav ul li a').addClass('cursor')
        }
        mouseMove = e.clientX;    
    })

    $('.logo-menu nav > ul > li .subMenu').click(function () {  
        $(this).prev('ul').slideToggle()
        // $('.logo-menu nav  ul ul').not($(this).prev('ul')).slideUp()
    })
})

document.addEventListener('scroll' , function () {     
    if(window.scrollY > 100){
        document.getElementById('header').classList.add('sticky')
    }else{
        document.getElementById('header').classList.remove('sticky')
    }
})
