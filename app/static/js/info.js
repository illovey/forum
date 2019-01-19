function show_box(sts, msg, time)
{
    if(sts == 'error'){
        var ele_box = '<div class="box_alert" style="width:280px;padding:10px;text-align:center;background-color:#D84C31;color:#fff;position:fixed;top:-10px;left:50%;z-index:100001;margin-left:-150px;box-shadow:1px 1px 5px #333;-webkit-box-shadow:1px 1px 5px #333;font-family:微软雅黑;">'+msg+'</div>';
    }else{
        var ele_box = '<div class="box_alert" style="width:280px;padding:10px;text-align:center;background-color:#5cb85c;color:#fff;position:fixed;top:-10px;left:50%;z-index:100001;margin-left:-150px;box-shadow:1px 1px 5px #333;-webkit-box-shadow:1px 1px 5px #333;font-family:微软雅黑;">'+msg+'</div>';
    }
    var ele_obj = $(".box_alert");
    $(".box_alert").remove();
    
    $('body').append(ele_box);
    $('.box_alert').fadeIn();
    $(".box_alert").animate({top:'50px'},function(){
    }); // 从上面掉落下来
    // shake('box_alert');
    window.setTimeout("box_clos()", time);//使用字符串执行方法 
}

function box_clos()
{
    $('.box_alert').fadeOut();
}

function shake(o)
{
    var $panel = $("."+o);
    box_left = ($(window).width() -  $panel.width()) / 2;
    $panel.css({'left': box_left,'position':'absolute'});
    for(var i=1; 3>=i; i++) {
        $panel.animate({left:box_left-(60-10*i)},100);
        $panel.animate({left:box_left+1*(60-10*i)},100);
    }
}