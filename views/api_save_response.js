var readPaoMessageContainer 			= document.createElement("div");
readPaoMessageContainer.id 				= "readPaoMessageContainer";
readPaoMessageContainer.style.position	= "fixed" 
readPaoMessageContainer.style.top		= "0px"
readPaoMessageContainer.style.width		= "100%"
readPaoMessageContainer.style.textAlign	= "center"
readPaoMessageContainer.style.zIndex	= "1000"

readPaoMessage 							= document.createElement("div");
readPaoMessage.id 						= "readPaoMessage";
readPaoMessage.style.backgroundColor	= "yellow"
readPaoMessage.style.margin				= "0px auto"
readPaoMessage.style.width				= "300px"
readPaoMessage.style.fontSize			= "13px"
readPaoMessageContainer.appendChild(readPaoMessage)

readPaoMessage.innerHTML = "You saved a url in list <b>${list_item.list_name}</b>!"

document.getElementsByTagName('body')[0].appendChild(readPaoMessageContainer);


readPaoFadeStep		= 1
readPaoFadeDelay	= 1

readPaoStayOnScreen = 1500;

readPaoFadeTimeout = false;

readPaoFadeIn()

function readPaoFadeIn() {
    if(readPaoFadeStep >= 100){
		window.clearTimeout(readPaoFadeTimeout);
		readPaoFadeTimeout = window.setTimeout("readPaoFadeOut()", readPaoStayOnScreen);
		return false;
    }
	    
    readPaoSetOpacity(readPaoMessage, (readPaoFadeStep/100));
    readPaoFadeStep++;
    readPaoFadeTimeout =  window.setTimeout("readPaoFadeIn()", readPaoFadeDelay);
}
function readPaoFadeOut() {
    if(readPaoFadeStep<1){
		window.clearTimeout(readPaoFadeTimeout);
		try {
			document.getElementsByTagName('body')[0].removeChild(document.getElementById('readPaoMessageContainer'));
		}catch(e) {
			readPaoMessageContainer.style.display	= "none"
			readPaoMessageContainer.innerHTML		= "";
		}
    }
    
    readPaoSetOpacity(readPaoMessage, (readPaoFadeStep/100));
    readPaoFadeStep--;
    readPaoFadeTimeout = window.setTimeout("readPaoFadeOut()", readPaoFadeDelay);
}

function readPaoSetOpacity( domElement, opacity){
    if(domElement.style.opacity != undefined){
        domElement.style.opacity = opacity;
    }else if( domElement.style.MozOpacity != undefined){
        domElement.style.MozOpacity = opacity;
    }else if ( domElement.style.filter != undefined){
        domElement.style.filter="alpha(opacity=" + Math.round(opacity * 100) + ")";
    }
} 

