document.write("<script  type='text/javascript'  src='http://ajax.microsoft.com/ajax/jquery/jquery-1.11.3.min.js'></script>");
/*
function search_city() {
    var xmlhttp = new XMLHttpRequest();
    var cityname = document.getElementById("cityname").value

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            document.getElementById("return").innerHTML = xmlhttp.responseText;
        }
    }
    xmlhttp.open("POST", "/search_city", true);
    //设置编码格式...........!!!!
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send("cityname=" + cityname);
    document.getElementById("return").innerHTML = xmlhttp.responseText;
}
*/


/*
function search_seven() {
    var xmlhttp = new XMLHttpRequest();
    var cityname = document.getElementById("cityname").value

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            document.getElementById("return").innerHTML = xmlhttp.responseText;
        }
    }
    xmlhttp.open("POST", "/search_seven", true);
    //设置编码格式...........!!!!
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send("cityname=" + cityname);
    document.getElementById("return").innerHTML = xmlhttp.responseText;
}
*/

$(function(){
    $('#sub').click(function(){
         $.ajax({
             type: "POST",
             url: "/search_seven",
             data: {cityname:$("#cityname").val() },
             dataType: "html",
             success: function(data){
                         $('#return').empty();   //清空resText里面的所有内容
                         var html = ''; 
                         $.each(data, function(commentIndex, comment){
                               html += '<div class="comment"><h6>' + comment['username']
                                         + ':</h6><p class="para"' + comment['content']
                                         + '</p></div>';
                         });
                         $('#return').html(html);
                      }
         });
    });
});


/*
$(document).ready(function() {
    $("#sub2").click(function() {
        var cn = document.getElementById("cityname").value
        $.post("/search_seven", {
                cityname: cn
            },
            function(data, status) {
                document.getElementById("return").innerHTML = data
            });
    });
});
*/

//    xmlhttp.onreadystatechange = function() {
//        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
//            document.getElementById("return").innerHTML = xmlhttp.responseText;
//        }
//    }
//    xmlhttp.open("POST", "/search_seven", true);
//    //设置编码格式...........!!!!
//    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//    xmlhttp.send("cityname=" + cityname);
//    document.getElementById("return").innerHTML = xmlhttp.responseText;
