// Create WebSocket connection.
const socket = new WebSocket("ws://localhost:5555");

// Connection opened
socket.addEventListener("open", function (event) {
	console.log("Connected to server");
});

// Connection closed
socket.addEventListener("close", function (event) {
	console.log("Disconnected from server");
});

// Listen for messages
socket.addEventListener("message", function (event) {
	// console.log("Message from server ", event.data);

	if (event.data == "1" || event.data == "0") {
		localStorage.setItem("colour", event.data == "1" ? "w" : "b");
		console.log(localStorage.getItem("colour"));

		if (event.data == "1") {
			set_token(true);
			// token = true;
		}
	} else if (event.data.includes("invalid")) {
		// a = JSON.parse(event.data)
		// console.log(a.invalid)
		console.log(event.data)
		// change_board(JSON.parse(event.data))
		set_token(true);
	} else if (event.data.includes("move")) {
		console.log(event.data)
		// ob = JSON.parse(event.dat/a)
		// console.log(ob.move)
		set_token(true);
		// change_board(event.data["move"])
	} else {
		console.log(event.data);
	}
});

// send pgn

function onmove(move, time, player) {
	a = { move: move, time: time, colour: player };
	a = JSON.stringify(a);
	socket.send(a);
	set_token(false);
	// document.getElementById("board").style.userSelect = "none"
	// document.getElementsByClassName("piece").style.userSelect = "none"
	// for(ob of document.getElementsByClassName("piece")){
	// 	ob.style.userSelect = "none"
	// }
	// $("#board").style.userSelect = "none"
	// console.log('{"move" : move, "time" : time, "colour" : player}')
}

function set_token(val) {
	localStorage.setItem("token", val);
}

function get_token() {
	return localStorage.getItem("token") == "true";
}
