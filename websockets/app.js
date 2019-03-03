const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 9000 });

wss.on('connection', function connection(ws, req) {

	ws.send('I see you are connected!');
	
	ws.on('message', function incoming(message) {
		// Log message received via WebSocket
		console.log('received: %s', message);

		//Send a response to the WebSocket message
		ws.send('Here is the data you just sent: '+message);

		// //Send Delayed Second Response
		// setTimeout(() => {
		// 	ws.send('Here is an unsolicited response to: '+message);
		// }, 5000);

	});

});

console.log('WebSocket Server listening on port 9000');