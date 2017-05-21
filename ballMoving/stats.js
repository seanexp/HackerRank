// Now some basic canvas stuff. Here we'll make a variable for the canvas and then initialize its 2d context for drawing
var canvas = document.getElementById("myCanvas"),
	ctx = canvas.getContext("2d");

// Now setting the width and height of the canvas
var W = $(window).width(),
	H = 450;

// Draw dots in canvas
var thirdLineY = 400,
	secondLineY = thirdLineY / 2,
	leftMostX = 50,
	rightMostX = W - 50;

var thirdLineDots = [[leftMostX, thirdLineY], [(leftMostX + rightMostX) / 2, thirdLineY], [rightMostX, thirdLineY]];

var secondLineDots = [[(thirdLineDots[0][0] + thirdLineDots[1][0]) / 2, secondLineY], [(thirdLineDots[1][0] + thirdLineDots[2][0]) / 2, secondLineY]];


// Applying these to the canvas element
canvas.height = H; canvas.width = W;

// First of all we'll create a ball object which will contain all the methods and variables specific to the ball.
// Lets define some variables first

var ball = {};

// The ball object
// It will contain the following details
// 1) Its x and y position
// 2) Radius and color
// 3) Velocity vectors
// 4) the method to draw or paint it on the canvas

ball = {
   x: W/2,
   y: 50,

   radius: 15,
   color: "blue",

   draw: function() {
	   // Here, we'll first begin drawing the path and then use the arc() function to draw the circle. The arc function accepts 6 parameters, x position, y position, radius, start angle, end angle and a boolean for anti-clockwise direction.
	   ctx.beginPath();
	   ctx.arc(this.x, this.y, this.radius, 0, Math.PI*2, false);
	   ctx.fillStyle = this.color;
	   ctx.fill();
	   ctx.closePath();
   }
};

// When we do animations in canvas, we have to repaint the whole canvas in each frame. Either clear the whole area or paint it with some color. This helps in keeping the area clean without any repetition mess.
// So, lets create a function that will do it for us.
function clearCanvas() {
	ctx.clearRect(0, 0, W, H);
}

// A function that will update the position of the ball is also needed. Lets create one
function update() {
	clearCanvas();
	ball.draw();

	// Now, lets make the ball move by adding the velocity vectors to its position
}

// Now, the animation time!
// in setInterval, 1000/x depicts x fps! So, in this casse, we are aiming for 60fps for smoother animations.
// setInterval(update, 1000/60);
ball.draw();

for (i = 0; i < thirdLineDots.length; i++) {
	var x = 0, y = 0;
	x = thirdLineDots[i][0];
	y = thirdLineDots[i][1];
	ctx.beginPath();
	ctx.rect(x, y, 5, 5);
	ctx.fillStyle = 'black';
	ctx.fill();
}

for (i = 0; i < secondLineDots.length; i++) {
	x = secondLineDots[i][0];
	y = secondLineDots[i][1];
	console.log(x);
	ctx.beginPath();
	ctx.rect(x, y, 5, 5);
	ctx.fillStyle = 'black';
	ctx.fill();
}

ctx.beginPath();
ctx.rect(W/2, 50, 5, 5);
ctx.fillStyle = 'black';
ctx.fill();

// ball move experiment
var locNum = 0,
	A = 0, B = 0, C = 0;

n = 10000; // number of actions

for (i = 0; i < n; i++) {
	for (j = 0; j < 2; j++) { // 2 = number of steps
		if (Math.random() >= 0.5) { locNum += 1; }
	}

	if (locNum == 0) { A += 1; }
	else if (locNum == 1) { B += 1; }
	else { C += 1; }

	locNum = 0;
}

// This completes the tutorial here. Try experimenting with different values to get a better understanding.

var data = [{
	x: ['A', 'B', 'C'],
	y: [A, B, C],
	type: 'bar'
}];

Plotly.newPlot('myDiv', data);

