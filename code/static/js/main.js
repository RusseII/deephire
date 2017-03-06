namespace = '';
// Connect to the Socket.IO server.
// The connection URL has the following format:
//     http[s]://<domain>:<port>[/<namespace>]
var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);
// Event handler for new connections.
// The callback function is invoked when a connection with the
// server is established.

function sendMessage() {
  var msg = document.getElementById('human-textbox').value;
  console.log(msg);

  populateHumanMessage(msg);

  socket.emit('message_sent', msg);
}

function populateAIMessage(msg) {
    var element = document.createElement('div');
    element.innerHTML = msg;
    element.className = 'chat-bubble ai-chat-bubble';

    document.getElementById("ai-chat-container").appendChild(element);
}

function populateHumanMessage(msg) {
    var element = document.createElement('div');
    element.innerHTML = msg;
    element.className = 'chat-bubble human-chat-bubble';
    //"<div class='chat-bubble ai-chat-bubble'>"+ msg +"</div>");
    document.getElementById("human-chat-container").appendChild(element);//.appendChild("<div class='chat-bubble ai-chat-bubble'>"+ msg +"</div>")
}

socket.on('message_recieved', function(msg) {
  populateAIMessage(msg);
});

socket.on('connect', function() {
  socket.emit('loaded');
});
