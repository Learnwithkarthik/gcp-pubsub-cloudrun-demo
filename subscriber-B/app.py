from flask import Flask, request
import base64
import json
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# GET – health check
@app.route("/", methods=["GET"])
def health():
    return "Subscriber-B is running", 200

# POST – Pub/Sub push endpoint
@app.route("/", methods=["POST"])
def receive_message():
    envelope = request.get_json()

    if not envelope or "message" not in envelope:
        logging.error("Invalid Pub/Sub message")
        return ("Bad Request", 400)

    message_data = base64.b64decode(
        envelope["message"]["data"]
    ).decode("utf-8")

    data = json.loads(message_data)

    logging.info(f"[SUBSCRIBER-B] Notification received: {data}")

    return ("OK", 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
