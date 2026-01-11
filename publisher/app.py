from flask import Flask
from google.cloud import pubsub_v1
import json

app = Flask(__name__)

PROJECT_ID = "terraform-482817"
TOPIC_ID = "orders-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

# GET – health check (browser friendly)
@app.route("/", methods=["GET"])
def health():
    return "Publisher is running", 200

# POST – actual publish logic
@app.route("/publish", methods=["POST"])
def publish():
    message = {
        "order_id": "ORD-5001",
        "status": "CREATED",
        "amount": 2999
    }

    publisher.publish(
        topic_path,
        json.dumps(message).encode("utf-8")
    )

    print("Published:", message)
    return "Message Published", 200
