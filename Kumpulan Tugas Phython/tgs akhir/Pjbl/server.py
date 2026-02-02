from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
import json
import paho.mqtt.client as mqtt

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

USER = {"username": "admin", "password": "123"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    req = request.json
    if req["username"] == USER["username"] and req["password"] == USER["password"]:
        return jsonify({"status": "ok"})
    return jsonify({"status": "fail"})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)