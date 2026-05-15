from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Payment Service Running"

@app.route("/payment")
def payment():
    notification_response = requests.get(
        "http://notification-service:5005/notify",
        timeout=3
    )

    return {
        "message": "Payment completed successfully",
        "notification": notification_response.json()
    }

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "payment-service"
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)