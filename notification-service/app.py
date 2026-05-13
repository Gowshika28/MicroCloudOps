from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Notification Service Running"

@app.route("/notifications")
def notifications():
    return jsonify([
        {
            "notification_id": 301,
            "type": "Email",
            "message": "Order placed successfully"
        },
        {
            "notification_id": 302,
            "type": "SMS",
            "message": "Payment received"
        }
    ])

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "notification-service"
    })

app.run(host="0.0.0.0", port=5005)