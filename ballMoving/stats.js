// Now setting the width and height of the canvas
var W = $(window).width(),
	H = $("#wrapper").height(),
	R = $("#ball").width();

// time interval
var interval = $("input[name='interval']")[0].value;
// var interval = 100;

// Draw dots in canvas
var thirdLineY = H -50,
	secondLineY = thirdLineY / 2,
	leftMostX = 50, rightMostX = W - 50;

var thirdLineDots = [
	[leftMostX, thirdLineY], 
	[(leftMostX + rightMostX) / 2, thirdLineY], 
	[rightMostX, thirdLineY]
];

var secondLineDots = [
	[(thirdLineDots[0][0] + thirdLineDots[1][0]) / 2, secondLineY], 
	[(thirdLineDots[1][0] + thirdLineDots[2][0]) / 2, secondLineY]
];

for (i = 0; i < thirdLineDots.length; i++) {
	//draw third line dots
}

for (i = 0; i < secondLineDots.length; i++) {
	//draw second line dots
}

var locDots = secondLineDots.concat(thirdLineDots);

function drawDots(dots) {
	var size = 5 
		color = '#000';
	for (i = 0; i < dots.length; i++) {
		$("#wrapper").append(
			$('<div></div>')
				.css('position', 'absolute')
				.css('top', dots[i][1])
				.css('left', dots[i][0] - size/2)
				.css('width', size)
				.css('height', size)
				.css('background-color', color)
				.css('border-radius', '50%')
		);

		console.log(dots[i]);
	}
}

// draw a top dot
var firstLoc = [W/2, 50];
var locs = [[firstLoc], secondLineDots, thirdLineDots];

function setLoc(step, locNum) {
	$("#ball").animate({
		top: locs[step][locNum][1] - R/2,
		left: locs[step][locNum][0] - R/2,
	}, interval);

}

$(document).ready(function () {
	console.log("ready");
	// initial settings
	$("#wrapper").width(W);
	setLoc(0, 0); // set origin

	drawDots(locDots);

	$("button").click(function() {
		experiment();
	})

});

function experiment() {
	// ball move experiment
	var locNum = 0,
		A = 0, B = 0, C = 0;

	var n = 100; // number of actions
	var n = $("input[name='action']")[0].value;
	var i = 0;
	(function loop() {

	 for (j = 0; j < 2; j++) { // 2 = number of steps
	 	setLoc(j, locNum);
		if (Math.random() >= 0.5) { locNum += 1; }
	 }

	 if (locNum == 0) { 
		 A += 1; 
		 $("#A").text("A: " + A);
	 }
	 else if (locNum == 1) { 
		 B += 1; 
		 $("#B").text("B: " + B);
	 }
	 else { 
		 C += 1; 
		 $("#C").text("C: " + C);
	 }

	 setLoc(2, locNum);

	 // setLoc(0,0);

	 i++;
	 if (i < n) {
		 setTimeout(loop, 3*interval);
	 } else {
		var data = [{
			x: ['A', 'B', 'C'],
			y: [A, B, C],
			type: 'bar'
		}];

		Plotly.newPlot('myDiv', data);
	 }

	 locNum = 0;
	})();
	}

// This completes the tutorial here. Try experimenting with different values to get a better understanding.


