// Create WebSocket connection.
const socket2 = new WebSocket("ws://localhost:5555");

// Connection opened
socket2.addEventListener("open", function (event) {
	console.log("Connected to server");
});

// Connection closed
socket2.addEventListener("close", function (event) {
	console.log("Disconnected from server");
});

// Listen for messages
socket2.addEventListener("message", function (event) {
	if (event.data == "1" || event.data == "0") {
		localStorage.setItem("colour", event.data == "1" ? "w" : "b");
		console.log(localStorage.getItem("colour"));

		if (event.data == "1") {
			set_token(true);
		}
	} else if (event.data.includes("invalid")) {
		document.getElementById("board").remove();
		a = document.createElement("div");
		a.id = "board";
		document.body.appendChild(a);
		set_board();
		ob = JSON.parse(event.data);
		for (c of ob.invalid) {
			change_board(c);
		}
		set_token(true);

	} else if (event.data.includes("move")) {
		ob = JSON.parse(event.data);
		console.log(ob.move);
		change_board(ob.move);
		set_token(true);

	} else if (event.data.includes("checkmate")) {
		ob = JSON.parse(event.data);
		console.log(ob.checkmate);
		console.log("Checkmate");
		change_board(ob.checkmate);
		alert("You have been Checkmated!")
	
	} else {
		console.log(event.data);
	}
});

// send pgn

function onmove(move, time, player) {
	a = { move: move, time: time, colour: player };
	a = JSON.stringify(a);
	socket2.send(a);
	set_token(false);
	// document.getElementById("board").style.userSelect = "none"
	// document.getElementsByClassName("piece").style.userSelect = "none"
	// for(ob of document.getElementsByClassName("piece")){
	// 	ob.style.userSelect = "none"
	// }
	// $("#board").style.userSelect = "none"
	// console.log('{"move" : move, "time" : time, "colour" : player}')
}


function init() {
	a = {init : [
			localStorage.getItem("player_id"),
			localStorage.getItem("game_id"),
		],}
	a= JSON.stringify(a)
	socket2.send(a)
}
function set_token(val) {
	localStorage.setItem("token", val);
}

function get_token() {
	return localStorage.getItem("token") == "true";
}

setTimeout(function () {
	console.log(localStorage.getItem("player_id"))
	init();
}, 200);
