var csrftoken = $("[name=csrfmiddlewaretoken]").val();


$(document).ready(function () {
  navSwitch();
  detailClick();
  //sideBarHightlight();
});

function navSwitch() {
  var pathname = window.location.pathname;
  if (pathname.indexOf("/addnew/")>0) {
    cleanNavActive();
    $($(".nav-link")[1]).addClass("active");
  } else{
    cleanNavActive();
    $($(".nav-link")[0]).addClass("active");
  }
}

function sideBarHightlight(){
  var pathname = window.location.pathname;
  if (pathname.indexOf("/Rentals/")>0) {
    cleanSideBar();
    $($(".sideBarItem")[1]).addClass("active");
  } else{
    cleanSideBar();
    $($(".sideBarItem")[0]).addClass("active");
  }
}

function cleanSideBar(){
    $(".sideBarItem").removeClass("active");
}

function cleanNavActive() {
  $(".nav-link").removeClass("active");
}

function showDetail(data){
    $(".mainBody").hide();
    $(".detailBody").show();
    $(".detailBody").html(
        detailBody(data)
    )
    backToMain();
}

function backToMain(){
    $(".backToMain").click(function(){
        $(".detailBody").empty();
        $(".mainBody").show();
        $(".detailBody").hide();
    })
}

function detailBody(data){
    var head = `<div class="row"><span class="material-icons backToMain">
                    keyboard_arrow_left
                    </span></div>`;
    var template = '<div class="detailMainDiv">';
    var content = JSON.parse(data)[0].fields;
    template = template+adddetailRow('Title',content.post_title)
                       +adddetailRow('Price',new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'CAD' }).format(content.post_price))
                       +adddetailRow('Description',content.post_text)
                       +adddetailRow('Contact Name',content.post_owner)
                       +adddetailRow('Contact Information',content.post_contact)
                       +'</div>'

    return head+template;
}

function adddetailRow(title,data){
    var template = '';
    if(title=="Title"){
        template = `<div class='row detailInfo `+title+`'>
                        `+data+`       
                    </div>`
    }else{
        template = `<div class='detailDivContainer'>
                        <div class='detailDiv `+title+`'>
                            <div class='detailTitle'>
                                `+title+`
                            </div>
                            <div class='detailInfo'>
                                `+data+`
                            </div>
                        </div>
                    </div>`
    }

    return template;
}

function detailClick() {
  $(".detailClick").click(function () {
    $.ajax({
      method: "POST",
      url: "/function/getData/",
      data: { id: this.id,
             csrfmiddlewaretoken:csrftoken },
    //   contentType:'application/json,charset=utf-8',
      success: function (res) {
        console.log(res);
        showDetail(res)
      },
    });
  });
}
