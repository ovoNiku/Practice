var randomColor = function(){
	var s = ''
	for (var i = 0; i < 3; i ++) {
			n = Math.floor(Math.random()*256)
			console.log(n);
			s += n
			s += ','
	}
	s=s.substring(0,s.length-1)
	return 'rgb(' + s + ')'
}

$(".color").on("mouseover","li",function(event){
    var target = $(event.target);
		var color = randomColor();
    target.css({"background-color": color});
})
