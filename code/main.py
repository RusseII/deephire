import os
from bot import chat 
from db import db
import subprocess
from flask import Flask,flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, send, emit, join_room, leave_room, \
            Namespace

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None


@app.route('/', methods=['GET', 'POST'] )
def upload_file():
    return render_template("index.html", async_mode=socketio.async_mode)

    
@socketio.on('message_sent')
def get_message(msg):
    db().query("INSERT INTO Messages VALUES (?)", (msg,))
    print msg
    socketio.emit("message_recieved", chat(msg), room=request.sid )
    return

@socketio.on('loaded')
def start(): 
    socketio.emit("message_recieved", chat("start"), room=request.sid)
    return
    
if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0') 
