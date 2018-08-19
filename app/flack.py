import os

from flask import Flask, render_template, jsonify, request, url_for, redirect, session, flash
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
app.secret_key = 'adamiscool'

@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html")
