readPaoSaveUrl = "http://localhost:8080/api/save"

bookmarkletTemplate = "javascript:(function(){readPao_list='%listName%';readpaoScript=document.createElement('script');readpaoScript.type='text/javascript';readpaoScript.src='" + readPaoSaveUrl + "?list='+readPao_list+'&url='+escape(window.location.href)+'&rand='+(Math.random());document.getElementsByTagName('head')[0].appendChild(readpaoScript);})();"



var listRe = new RegExp("^[a-zA-Z0-9]*$")

function clearMessage(){
    $("#message").hide().removeClass('messageGood').removeClass('messageBad').html("")
}

$(document).ready(function(){




    $("#list").keypress(function(event){
        if (event.keyCode == 13) { // daca s-a apasat enter sa nu face submit
            return false;
        }
    })
    
    $("#list").keyup(function(){
        listValue = $(this).attr('value')
        
        clearMessage()
        if (listRe.test(listValue) && listValue != '') {
            $("#message").show().addClass("messageGood").html("List name is great!")

            bookmarklet = bookmarkletTemplate.replace("%listName%", listValue)
            
            $('#bookmarkletContainer').show();
            $('#bookmarklet').attr('href', bookmarklet)

        }
        else {
	        clearMessage()

            $("#message").show().addClass("messageBad").html("List name is not good! (Only letters and numbers)")
	        $('#bookmarkletContainer').hide();
	        $('#bookmarklet').attr('href', '#')

        }
        
    })
    
    $("#list").focus(function(){
        clearMessage()
        //$('#bookmarkletContainer').hide();
        //$('#bookmarklet').attr('href', '#')
        
    })
    
});
