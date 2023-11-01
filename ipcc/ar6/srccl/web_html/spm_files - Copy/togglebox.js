(function($){function togglebox(item,options){var defaults={off:'Off',on:'On',debug:false};this.options=$.extend(true,defaults,options);this.item=$(item);this.init();}
togglebox.prototype={init:function(){var plugin_instance=this;var plugin_item=this.item;var plugin_settings=plugin_instance.options;var plugin_elements=plugin_settings.elements;if(plugin_settings.debug==true){console.log('initializing toggle');console.log('item',plugin_item);}
var init_state='off';if(plugin_item.is(':checked')){init_state='on';}
var box_class='';if(plugin_item.prop('disabled')){box_class+='disabled';}
var box=$('<div class="togglebox '+box_class+'" data-state="'+init_state+'" />');box.insertAfter(plugin_item);var on_text=plugin_settings.on;if(typeof plugin_item.attr('data-on')!='undefined'){on_text=plugin_item.attr('data-on');}
var off_text=plugin_settings.off;if(typeof plugin_item.attr('data-off')!='undefined'){off_text=plugin_item.attr('data-off');}
var markup=$('<div class="togglebox-track"><span class="on">'+on_text+'</span><span class="switch"></span><span class="off">'+off_text+'</span></div>');markup.appendTo(box);plugin_item.addClass('togglebox-input');plugin_item.parents('label').click(function(e){e.preventDefault();});box.click(function(){if(!plugin_item.prop('disabled')){if($(this).attr('data-state')=='off'){$(this).attr('data-state','on');}else{$(this).attr('data-state','off');}
plugin_item.prop("checked",!plugin_item.prop("checked")).change();}});},toggle:function(fn_options){var plugin_instance=this;var plugin_item=this.item;var plugin_settings=plugin_instance.options;var plugin_elements=plugin_settings.elements;var defaults={action:'on'};var settings=$.extend(true,defaults,fn_options);}}
$.fn.togglebox=function(opt){var args=Array.prototype.slice.call(arguments,1);return this.each(function(){var item=$(this);var instance=item.data('togglebox');if(!instance){item.data('togglebox',new togglebox(this,opt));}else{if(typeof opt==='string'){instance[opt].apply(instance,args);}}});}}(jQuery));