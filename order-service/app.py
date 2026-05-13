from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Order Service Running"

@app.route("/orders")
def orders():
    return jsonify([
        {
            "order_id": 101,
            "product": "Laptop",
            "status": "Placed"
        },
        {
            "order_id": 102,
            "product": "Phone",
            "status": "Shipped"
        }
    ])

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "order-service"
    })

app.run(host="0.0.0.0", port=5003)