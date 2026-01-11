from flask import Flask
from google.cloud import pubsub_v1
import json

app = Flask(__name__)

PROJECT_ID = "YOUR_PROJECT_ID"
TOPIC_ID = "orders-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

@app.route("/publish", methods=["POST"])
def publish():
    message = {
        "order_id": "ORD-2001",
        "amount": 3499,
        "status": "CREATED"
    }

    publisher.publish(
        topic_path,
        json.dumps(message).encode("utf-8")
    )

    return "Message Published", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
