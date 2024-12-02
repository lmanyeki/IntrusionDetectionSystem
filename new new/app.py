from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import csv
import random

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Simulated real-time traffic
REALTIME_DATA = [
    {"source": "192.168.0.1", "threat": "High"},
    {"source": "192.168.0.2", "threat": "Medium"},
    {"source": "192.168.0.3", "threat": "Low"},
]

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"message": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"message": "No file selected"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return jsonify({"message": "File uploaded successfully!"}), 200

@app.route("/get-uploaded-data", methods=["GET"])
def get_uploaded_data():
    # Retrieve the most recently uploaded file
    files = sorted(
        [os.path.join(UPLOAD_FOLDER, f) for f in os.listdir(UPLOAD_FOLDER)],
        key=os.path.getctime,
    )
    if not files:
        return jsonify([])

    latest_file = files[-1]
    with open(latest_file, "r") as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    return jsonify(data)

@app.route("/analyze", methods=["GET"])
def analyze_data():
    # Simulate real-time analysis
    results = [random.choice(REALTIME_DATA) for _ in range(5)]
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
