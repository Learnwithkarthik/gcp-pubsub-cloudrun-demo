from flask import Flask, request
import base64
import json
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/", methods=["POST"])
def receive_message():
    envelope = request.get_json()

    if not envelope or "message" not in envelope:
        logging.error("Invalid Pub/Sub message format")
        return ("Bad Request", 400)

    pubsub_message = envelope["message"]

    message_data = base64.b64decode(
        pubsub_message["data"]
    ).decode("utf-8")

    data = json.loads(message_data)

    # IMPORTANT: Unique log line to distinguish Subscriber-B
    logging.info(f"[SUBSCRIBER-B] Notification service received: {data}")

    return ("OK", 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
