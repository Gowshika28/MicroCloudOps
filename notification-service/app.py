from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Notification Service Running"

@app.route("/notify")
def notify():
    return {
        "message": "Notification sent successfully",
        "type": "payment-confirmation"
    }

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "notification-service"
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)