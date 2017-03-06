import os
from bot import chat 
import subprocess
from flask import Flask,flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, send, emit, join_room, leave_room, \
            Namespace

UPLOAD_FOLDER = 'upload_folder/'
async_mode = None

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None


@app.route('/', methods=['GET', 'POST'] )
def upload_file():
    return render_template("index.html", async_mode=socketio.async_mode)

#@socketio.on('loaded')
#def page_load():
#    newvisitor()
#    newprint()
#

@socketio.on('message_sent')
def get_message(msg):
    socketio.emit("message_recieved", chat(msg))
    
	 
def newvisitor():
    visitors = db().query("SELECT visits FROM stats")[0][0]
    socketio.emit('visitor_update',
            {'data': visitors})
    print (visitors)
    return

def newprint():
    prints = db().query("SELECT print_jobs FROM stats")[0][0]
    socketio.emit('print_job_update',
            {'data': prints})
    return

if __name__ == "__main__":
    socketio.run(app, debug=True) 
