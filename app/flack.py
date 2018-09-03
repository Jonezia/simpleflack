import os

from flask import Flask, render_template, jsonify, request, url_for, redirect, session, flash
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
app.secret_key = 'adamiscool'

channels = ["TeamFlack"]

@app.route("/", methods=['GET','POST'])
def index():
    return redirect(url_for('channel',channelname="TeamFlack", channels=channels))

@app.route("/channel/<string:channelname>")
def channel(channelname):
    return render_template("index.html",channelname=channelname, channels=channels)

@socketio.on('new channel')
def newchannel(channelname):
    channels.append(channelname)
    emit("update channels", broadcast = True)
