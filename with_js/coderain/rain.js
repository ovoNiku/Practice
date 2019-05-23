var config = {
		background: 'rgba(0,0,0,0.1)',
		font_size: 16,
		font: '16px arial',
		color: 	'#CDB7B5',
		charsArr: '0123456789qwertyuiopasdfghjklzxcvbnm'.split(''),
		density: 0.95,
		charArray: (chars) => {
			return chars[Math.floor(Math.random() * chars.length)]
		},
}

var init = () => {
		let canvas = document.querySelector('#canvas')
		canvas.width = screen.width
		canvas.height = screen.height
		let columns = Math.floor(canvas.width / config.font_size)
		let boult = new Array(columns).fill(1)
		canvas.addEventListener("click", function(){
				console.log("click!");
				var docEle = document.documentElement;
				var rfs = docEle.requestFullScreen || docEle.webkitRequestFullScreen || docEle.mozRequestFullScreen || docEle.msRequestFullScreen;
				if (rfs) {
					rfs.call(docEle);
				} else {
					console.log("your browser doesn't support fullscr.");
				}
		})
		let context = canvas.getContext('2d')
		return  {
		      canvas, context, boult
		    }
}

var draw = (canvas, context, boult) => {
		let { background, color, font_size, font, charsArr, density, charArray } = config
    context.fillStyle = background
    context.fillRect(0, 0, canvas.width, canvas.height)
    context.fillStyle = color
    context.font = font
		for(let i = 0; i < boult.length; i++) {
				let text = charArray(charsArr)
	      let posX = i*font_size
	      let posY = boult[i]*font_size
	      context.fillText(text, posX, posY)
				if(posY > screen.height || Math.random() > density) {
	        	boult[i] = 0
	      }
	      boult[i]++
		}
}

var __main = () => {
    let {canvas, context, boult} = init()
    setInterval(()=>{
      draw(canvas, context, boult)
    }, 1000/40)
}

__main()
