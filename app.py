from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
import random
import time
import threading
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)  # Enable CORS for all routes
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow any origin for SocketIO

@app.route("/")
def home():
    return "SocketIO server is running."

if __name__ == "__main__":
    socketio.run(app, debug=True)


app = Flask(__name__)
socketio = SocketIO(app)

# Global variable to control data generation
stop_generation = False

# Simulated Real-Time Data Generator
def generate_realtime_data():
    global stop_generation
    while not stop_generation:
        # Simulated data
        data = {
            "Duration": round(random.uniform(0.1, 10.0), 2),
            "Protocol_Type": random.choice(["TCP", "UDP", "ICMP"]),
            "Service": random.choice(["http", "smtp", "ftp"]),
            "Flag": random.choice(["SF", "S0", "REJ"]),
            "src_bytes": random.randint(0, 10000),
            "dst_bytes": random.randint(0, 10000),
            "Class": random.choice(["Normal", "DoS", "Probe", "R2L", "U2R"])
        }
        # Emit data to the front end
        socketio.emit('realtime_data', data)
        time.sleep(5)  # Generate every 5 seconds

# Endpoint to stop data generation
@app.route('/stop', methods=['POST'])
def stop():
    global stop_generation
    stop_generation = True
    return jsonify({"message": "Data generation stopped."})

# Start background thread for real-time data generation
@socketio.on('connect')
def on_connect():
    print("Client connected!")
    global stop_generation
    stop_generation = False
    thread = threading.Thread(target=generate_realtime_data)
    thread.start()

if __name__ == '__main__':
    socketio.run(app, debug=True)
