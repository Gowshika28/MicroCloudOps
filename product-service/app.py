from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Product Service Running"

@app.route("/product")
def product():
    return {
        "product_name": "Laptop",
        "price": 75000,
        "stock": "Available"
    }

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "product-service"
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)