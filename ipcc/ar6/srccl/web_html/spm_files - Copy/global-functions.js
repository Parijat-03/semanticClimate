document.documentElement.classList.remove('no-js');if(window.location.hash!=''){var init_scroll=window.location.hash;if(document.getElementById(init_scroll.substr(1))!==null){history.replaceState(null,document.title,location.protocol+'//'+location.host+location.pathname);console.log('scroll to '+init_scroll);}}
var site_url='//'+window.location.host+'/';theme_dir=site_url+'site/assets/themes/ipcc-report';var sticky_offset=0,scroll_offset=0;function is_empty(obj){for(var key in obj){if(obj.hasOwnProperty(key))
return false;}
return true;}
(function($){$(function(){if($('meta[property="fb:app_id"]').length){window.fbAsyncInit=function(){FB.init({appId:$('meta[property="fb:app_id"]').attr('content'),autoLogAppEvents:true,xfbml:true,version:'v3.2'});};(function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(d.getElementById(id)){return;}
js=d.createElement(s);js.id=id;js.src="https://connect.facebook.net/en_US/sdk.js";fjs.parentNode.insertBefore(js,fjs);}(document,'script','facebook-jssdk'));}
if($('body').hasClass('admin-bar')){sticky_offset+=32;scroll_offset+=32;}
$('#header-primary').stick_in_parent({parent:'body',offset_top:sticky_offset});console.log('sticky header');var header_height=$('#header-primary').outerHeight();sticky_offset+=header_height;scroll_offset+=header_height;$('.lazy').Lazy({effect:'fadeIn',effectTime:500,threshold:300});$('.lazy-bg').Lazy({effect:'fadeIn',effectTime:500,threshold:300});console.log('lazy');$('.smooth-scroll').click(function(e){var link_href=$(this).attr('href');e.preventDefault();console.log('smooth scroll to '+link_href);$(document).smooth_scroll({id:link_href,speed:2000,ease:'easeInOutQuart',offset:scroll_offset});});console.log('smooth scroll');if(init_scroll){if($(init_scroll).length){setTimeout(function(){console.log('smooth scroll');console.log(init_scroll);$(document).smooth_scroll({id:init_scroll,speed:2000,ease:'easeInOutQuart',offset:scroll_offset});},1000);}}
console.log('init scroll');$(document).nav_overlay({elements:{trigger:$('.menu-trigger')},open_fn:function(){},close_fn:function(){}});console.log('nav overlay');var social_accounts=JSON.parse($('#header-social').attr('data-accounts'));$('#share').share_widget({site_url:'//'+window.location.hostname,theme_dir:null,share_url:window.location.href,title:document.title,elements:{facebook:{display:true,label:'Facebook',icon:'icon-social-facebook'},twitter:{display:true,label:'Twitter',icon:'icon-social-twitter',text:null,via:social_accounts.twitter},pinterest:{display:false,label:'Pinterest',icon:'icon-social-pinterest'},permalink:{display:true,label:'Copy Permalink',icon:'icon-permalink'}},callback:null});$('#follow').follow_widget({elements:{twitter:{url:'https://twitter.com/'+social_accounts.twitter,icon:'icon-social-twitter'},facebook:{url:'https://facebook.com/'+social_accounts.facebook,icon:'icon-social-facebook'},instagram:{url:'http://instagram.com/'+social_accounts.instagram,icon:'icon-social-instagram'},linkedin:{url:'http://linkedin.com/'+social_accounts.linkedin,icon:'icon-social-linkedin'},youtube:{url:'http://youtube.com/'+social_accounts.youtube,icon:'icon-social-youtube'}}});$('.share').each(function(){var share_url=$(this).attr('data-share-url'),share_title=$(this).parents('.section-head').find('.section-title').text();$(this).share_widget({site_url:'//'+window.location.hostname,theme_dir:null,share_url:share_url,title:share_title,elements:{facebook:{display:true,label:'Facebook',icon:'icon-social-facebook'},twitter:{display:true,label:'Twitter',icon:'icon-social-twitter',text:share_title+' — '+document.title+' via @'+social_accounts.twitter+': ',via:social_accounts.twitter},permalink:{display:true,label:'Copy Permalink',icon:'icon-permalink'}},callback:null});});console.log('social widgets');$('.overlay-slider').slick();console.log('slick');$('.accordion-head').click(function(){var accordion=$(this).next('.accordion-content');if($(this).hasClass('accordion-open')){$(this).removeClass('accordion-open');accordion.removeClass('accordion-open');accordion.slideUp();}else{$(this).addClass('accordion-open');accordion.addClass('accordion-open');accordion.slideDown();}});console.log('accordion');if($('.type-supplements').length){$('.type-supplements').supplements({logging:true});var close_btn_offset=20+sticky_offset;$('.type-supplements .close-btn').stick_in_parent({offset_top:close_btn_offset});}
console.log('supplements');if($('#grid-content').length){$('#grid-content').filter_grid();}
console.log('filter grid');if($('.figure-dl-type').length){$('.figure-dl-type').togglebox({off:'SD',on:'HD',debug:false});}
$('.figure-dl-type').change(function(){console.log('changed');var dl_href=$(this).attr('data-val-off');if($(this).prop('checked')){dl_href=$(this).attr('data-val-on');}
$(this).parents('.figure-download').find('.figure-dl-link').attr('href',dl_href);});});})(jQuery);