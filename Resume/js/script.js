const seagull = document.getElementById('seagull');
const name = document.querySelector("#name");
var x = false;
name.addEventListener("click", function(){
	if(x == false){
		$('#seagull').animate({
			left: '1000px',
			top: '0px'
		}, 2000, function(){
			$('#seagull').css({"left": "-100px", 
			"top": "-100px",});
		})
		x = true;

	}else{
		$('#seagull').animate({
			left: '60px',
			top: '60px'
		}, 1000)  
		x = false;
	}
}, false)

var y = 0;
var time;
name.addEventListener("mouseenter", function(){
	time = setInterval(function(){
		if(y % 2){
			name.style.fontWeight = "700";

		}else{
			name.style.fontWeight = "500";
		}
		y++;
	}, 200)

}, false)

name.addEventListener("mouseleave", function(){
	clearInterval(time)
}, false)
