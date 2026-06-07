from flask import Flask, request, jsonify
import csv
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "iot_data.csv"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "device_id",
            "location",
            "temperature",
            "humidity",
            "air_quality",
            "traffic_density",
            "timestamp"
        ])

@app.route("/")
def home():
    return "Smart City IoT Backend is running."

@app.route("/data", methods=["POST"])
def receive_data():
    data = request.get_json()

    with open(DATA_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            data["device_id"],
            data["location"],
            data["temperature"],
            data["humidity"],
            data["air_quality"],
            data["traffic_density"],
            data["timestamp"]
        ])

    return jsonify({"message": "Data received successfully", "data": data}), 201

@app.route("/data", methods=["GET"])
def get_data():
    rows = []

    with open(DATA_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)