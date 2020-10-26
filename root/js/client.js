// Create WebSocket connection.
// const socket = new WebSocket("ws://localhost:5555");

// Connection opened
// socket.addEventListener("open", function (event) {
// 	console.log("Connected to server");
// });

// // Connection closed
// socket.addEventListener("close", function (event) {
// 	console.log("Disconnected from server");
// });

// // Listen for messages
// socket.addEventListener("message", function (event) {
// 	console.log("Message from server ", event.data);
// });


// send pgn

// function onmove(move, time, player){
// 	a = {"move" : move, "time" : time, "colour" : player}
// 	a= JSON.stringify(a)
// 	console.log(a)
// 	socket.send(a)
// 	// console.log('{"move" : move, "time" : time, "colour" : player}')
// }