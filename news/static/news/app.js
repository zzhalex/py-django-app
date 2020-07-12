var csrftoken = $("[name=csrfmiddlewaretoken]").val();


$(document).ready(function () {
  navSwitch();
  detailClick();
});

function navSwitch() {
  var pathname = window.location.pathname;
  if (pathname == "/") {
    cleanNavActive();
    $($(".nav-link")[0]).addClass("active");
  } else if (pathname == "/addnew/") {
    cleanNavActive();
    $($(".nav-link")[1]).addClass("active");
  }
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
                       +adddetailRow('Price',content.post_price)
                       +adddetailRow('Description',content.post_text)
                       +adddetailRow('Time',content.pub_date)
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
        template = `<div class='detailDiv `+title+`'>
                        <div class='detailTitle'>
                            `+title+`
                        </div>
                        <div class='detailInfo'>
                            `+data+`
                        </div>
                    </div>`
    }

    return template;
}

function detailClick() {
  $(".detailClick").click(function () {
    $.ajax({
      method: "POST",
      url: "getData/",
      data: { id: this.id,
             csrfmiddlewaretoken:csrftoken },
      //contentType:'application/json,charset=utf-8',
      success: function (res) {
        console.log(res);
        showDetail(res)
      },
    });
  });
}
