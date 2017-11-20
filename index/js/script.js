var x = $(window).width();
var y =$(window).height();
$('header').css('height', y+"px");

var a = Math.random()*x;
var b = Math.random()*y;


// $('.introduce a').click(function(){
// 	// $('.introduce a').css('color', 'black');
// })

$('canvas').css({'width': x+"px",
				'height': y+"px"});

// $('canvas').click(function(event) {
// 	$(this).mousemove(function(e){
// 		var c = document.getElementById("canvas");
// 		var ctx = c.getContext("2d");
// 		ctx.fillStyle = "#FFFFFF";
// 		ctx.fillRect(e.pageX,e.pageY,50,50);
// 		console.log(e.pageX,e.pageY);
// 	})
// });

// $('canvas').mousemove(function(e){
// 	var c = document.getElementById("canvas");
// 	var ctx = c.getContext("2d");
// 	var a = e.pageX;
// 	var b = e.pageY;
// 	$('canvas').click(function(){
// 		ctx.fillStyle = "#FFFFFF";
// 		ctx.fillRect(0,0,50,50);
// 		console.log(e.pageX,e.pageY);
// 	})
// });

// $('canvas').click(function(e){
// 	var c = document.getElementById("canvas");
// 	var ctx = c.getContext("2d");
// 	var box = c.getBoundingClientRect();
// 	var m = (e.clientX-box.left)*(c.width/box.width);
//     var n = (e.clientY-box.top)*(c.height/box.height); 
// 	ctx.fillStyle = "#FFFFFF";
// 	ctx.fillRect(m,n,10,10);
// 	console.log(m,n);
// })

var i = 0;
$('header').mousemove(function(e){
	i++;
	let m = i;
	$(this).append('<p class="drop" id="'+m+'"></p>');
	var w = Math.random()*40 + 10;
	$('#'+m).css({'right': window.innerWidth - e.clientX-25,
						'bottom': window.innerHeight - e.clientY-25});
	var t = Math.random()*800+500;
	$('#'+m).animate({
		opacity: 1,
		paddingLeft: w,
		paddingRight: w,
		paddingTop: w,
		paddingBottom: w},
		t, function(){
		$(this).animate({
			opacity: 0,
			paddingLeft: 0,
			paddingRight: 0,
			paddingTop: 0,
			paddingBottom: 0},
			t*2,function(){
				$('p').remove('#'+m);
		});
	});
})

$('.introduce a').css({'margin-top': y/2.5+"px"});
$('.introduce a').css({'opacity': "1"});

var n1 = false;
var n2 = false;
var n3 = false;

$('.projects #p1').click(function(){
	if(n1 == false){
		$('.projects #p1').slideUp(400,function(){
			$('.projects #n1').prepend("<h1>photo process</h1>");
			$('.projects #n1').css({"left":"0px"})
		});
		n1 = true;
	}
})

$('.projects #p2').click(function(){
	if(n2 == false){
		$('.projects #p2').slideUp(400,function(){
			$('.projects #n2').prepend("<h1>mooncake test</h1>");
			$('.projects #n2').css({"left":"0px"})
		});
		n2= true;
	}
})

$('.projects #p3').click(function(){
	if(n3 == false){
		$('.projects #p3').slideUp(400,function(){
			$('.projects #n3').prepend("<h1>resume</h1>");
			$('.projects #n3').css({"left":"0px"})
		});
		n3 = true;
	}
})


$('.projects #n1').click(function(){
	if(n1 == true){
		$('.projects #n1').css('left', '-300px')
		setTimeout(function(){
			$('.projects #n1').empty();
			$('.projects #p1').slideDown()}
			,500);
		n1 = false;
	}
})

$('.projects #n2').click(function(){
	if(n2 == true){
		$('.projects #n2').css('left', '-300px')
		setTimeout(function(){
			$('.projects #n2').empty();
			$('.projects #p2').slideDown()}
			,500);
		n2 = false;
	}
})

$('.projects #n3').click(function(){
	if(n3 == true){
		$('.projects #n3').css('left', '-300px')
		setTimeout(function(){
			$('.projects #n3').empty();
			$('.projects #p3').slideDown()}
			,500);
		n3 = false;
	}
})