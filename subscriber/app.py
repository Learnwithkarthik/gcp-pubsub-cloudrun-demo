from flask import Flask, request
import base64
import json
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# GET – health check
@app.route("/", methods=["GET"])
def health():
    return "Subscriber-A is running", 200

# POST – Pub/Sub push endpoint
@app.route("/", methods=["POST"])
def receive_message():
    logging.error("[SUBSCRIBER-A] Simulated failure")
    return ("Subscriber-A is down", 500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
