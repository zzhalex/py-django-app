$(document).ready(function(){
	navSwitch();
});

function navSwitch(){
    var pathname = window.location.pathname;
    if(pathname=='/'){
        cleanNavActive();
        $($(".nav-link")[0]).addClass("active");
    }else if(pathname=='/addnew/'){
        cleanNavActive();
        $($(".nav-link")[1]).addClass("active");
    }
}

function cleanNavActive(){
    $(".nav-link").removeClass("active");
}