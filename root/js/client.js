// Create WebSocket connection.
const socket = new WebSocket("ws://192.168.0.5:5555");

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

	if(event.data == "b" ||  event.data =="w"){
		localStorage.setItem("colour", event.data)
		console.log(localStorage.getItem("colour"))

		if(event.data == "w"){
			token = true;
		}
		else{
			token = false;
		}

	}

	else if(event.data == "false"){
		set_board(event.data)
		token = true;
	}
	console.log(token)
});


// send pgn

function onmove(move, time, player){
	a = {"move" : move, "time" : time, "colour" : player}
	a= JSON.stringify(a)
	console.log(a)
	socket.send(a)
	token = false;
	// document.getElementById("board").style.userSelect = "none"
	// document.getElementsByClassName("piece").style.userSelect = "none"
	for(ob of document.getElementsByClassName("piece")){
		ob.style.userSelect = "none"
	}
	// $("#board").style.userSelect = "none"
	// console.log('{"move" : move, "time" : time, "colour" : player}')
}