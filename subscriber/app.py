from flask import Flask, request
import base64
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def receive_message():
    envelope = request.get_json()
    if not envelope or "message" not in envelope:
        return ("Bad Request", 400)

    msg = envelope["message"]["data"]
    decoded = base64.b64decode(msg).decode("utf-8")
    data = json.loads(decoded)

    print("Received order:", data)
    return ("OK", 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
