document.documentElement.classList.remove('no-js');var site_url='//'+window.location.host+'/';theme_dir=site_url+'site/assets/themes/ipcc-report';(function($){$(function(){function set_overlay_height(){var overlay_header_height=$('#nav-overlay-header').outerHeight();if($('body').hasClass('admin-bar')){overlay_header_height+=32;}
$('#nav-overlay-content').css('height','calc(100vh - '+overlay_header_height+'px)');}
set_overlay_height();$(window).resize(function(){set_overlay_height();});$('#overlay-slider ul:not(.menu-level-1)').hide();$('#overlay-slider .accordion-menu li').each(function(){if($(this).find('.accordion-menu').length){$(this).addClass('has-child');$(this).find('.accordion-icon').first().find('i').addClass('icon-chevron-right');}});$('.accordion-menu .accordion-icon').click(function(){var accordion_li=$(this).closest('li');var accordion_item=$(this).closest('.accordion-item');var accordion_child=accordion_item.siblings('.accordion-menu');if(accordion_item.siblings('.accordion-menu').length){if(accordion_li.hasClass('open')){accordion_li.removeClass('open');accordion_child.slideUp();}else{accordion_li.addClass('open');accordion_child.slideDown();}}});$('.accordion-menu a').click(function(e){var link_href=$(this).attr('href');if(!$('body').hasClass('home')&&link_href.indexOf(window.location.pathname)!==-1){e.preventDefault();var hash_location=link_href.indexOf('#');var scroll_id=link_href.substr(hash_location);$(document).nav_overlay('hide_overlay');$(document).smooth_scroll({id:scroll_id,speed:2000,ease:'easeInOutQuart',offset:$('#header-primary').outerHeight()});}});});})(jQuery);