from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "API Gateway Running",
        "routes": {
            "product": "/product",
            "order": "/order",
            "payment": "/payment",
            "notification": "/notification",
            "health": "/health"
        }
    }

@app.route("/product")
def product():
    response = requests.get("http://product-service:5002/product")
    return response.json()

@app.route("/order")
def order():
    response = requests.get("http://order-service:5003/create-order")
    return response.json()

@app.route("/payment")
def payment():
    response = requests.get("http://payment-service:5004/payment")
    return response.json()

@app.route("/notification")
def notification():
    response = requests.get("http://notification-service:5005/notify")
    return response.json()

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "api-gateway"
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)