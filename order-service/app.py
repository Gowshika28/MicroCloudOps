from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Order Service Running"

@app.route("/create-order")
def create_order():
    product_response = requests.get("http://product-service:5002/product")

    return {
        "message": "Order created successfully",
        "product_details": product_response.json()
    }

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "order-service"
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)