from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import requests

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///orders.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

order_requests = Counter(
    "order_service_requests_total",
    "Total requests to Order Service"
)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    status = db.Column(db.String(50))

@app.route("/")
def home():
    order_requests.inc()
    return "Order Service Running"

@app.route("/create-order")
def create_order():
    order_requests.inc()

    product_response = requests.get("http://product-service:5002/product")
    product_data = product_response.json()

    order = Order(
        product_name=product_data.get("product_name", "Unknown"),
        price=product_data.get("price", 0),
        status="Order Created"
    )

    db.session.add(order)
    db.session.commit()

    return {
        "message": "Order created successfully",
        "order_id": order.id,
        "product_name": order.product_name,
        "price": order.price,
        "status": order.status
    }

@app.route("/orders")
def get_orders():
    order_requests.inc()

    orders = Order.query.all()

    return [
        {
            "order_id": order.id,
            "product_name": order.product_name,
            "price": order.price,
            "status": order.status
        }
        for order in orders
    ]

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "order-service"
    }, 200

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)