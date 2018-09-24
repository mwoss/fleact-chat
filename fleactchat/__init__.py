from flask import Flask, Session
from flask_socketio import SocketIO

app = Flask(__name__, static_folder="./frontend/static/js", template_folder="./frontend/static")
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'm\x15C\xe7\xcd)\xf0\x98"\x0c\x87E\x15\xf5\'\xd7\x03\xa9\x89\x1a\x80W\x95s\xc6\x1e7d;\xc6'

Session(app)
socketio = SocketIO(app, manage_session=False)

from fleactchat.server import views
