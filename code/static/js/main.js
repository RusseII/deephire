namespace = '';
// Connect to the Socket.IO server.
// The connection URL has the following format:
//     http[s]://<domain>:<port>[/<namespace>]
var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);
// Event handler for new connections.
// The callback function is invoked when a connection with the
// server is established.

// Bind send message to text box

document.getElementById("human-textbox")
    .addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode == 13) {
        sendMessage();
    }
});

function sendMessage() {
  var msg = document.getElementById('human-textbox').value;
  console.log(msg);

  // Exit if input is empty
  if (!msg.trim() || msg.trim() == '') return;

  // Populate message in chat container
  populateHumanMessage(msg);

  // Clear input value
  document.getElementById('human-textbox').value = '';

  // Scroll to bottom of chat
  var chatCtn = document.getElementById("chat-container");
  chatCtn.scrollTop = chatCtn.scrollHeight;

  socket.emit('message_sent', msg);
}

function populateAIMessage(msg) {
    var element = document.createElement('div');
    element.innerHTML = msg;
    element.className = 'chat-bubble ai-chat-bubble';

    document.getElementById("chat-container").appendChild(element);
}

function populateHumanMessage(msg) {
    var element = document.createElement('div');
    element.innerHTML = msg;
    element.className = 'chat-bubble human-chat-bubble';
    //"<div class='chat-bubble ai-chat-bubble'>"+ msg +"</div>");
    document.getElementById("chat-container").appendChild(element);//.appendChild("<div class='chat-bubble ai-chat-bubble'>"+ msg +"</div>")
}

socket.on('message_recieved', function(msg) {
  populateAIMessage(msg);
});

socket.on('connect', function() {
  socket.emit('loaded');
});
