from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

product_requests = Counter(
    "product_service_requests_total",
    "Total requests to Product Service"
)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    stock = db.Column(db.String(50))

@app.route("/")
def home():
    product_requests.inc()
    return "Product Service Running"

@app.route("/product")
def product():
    product_requests.inc()

    product = Product.query.first()

    if product:
        return {
            "id": product.id,
            "product_name": product.name,
            "price": product.price,
            "stock": product.stock
        }

    return {"message": "No product found"}

@app.route("/add-product")
def add_product():
    product_requests.inc()

    product = Product(
        name="Laptop",
        price=75000,
        stock="Available"
    )

    db.session.add(product)
    db.session.commit()

    return {"message": "Product added successfully"}

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "product-service"
    }, 200

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)