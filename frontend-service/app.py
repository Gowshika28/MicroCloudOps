from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>MicroCloudOps E-Commerce Platform</h1>

    <h2>Available Services</h2>

    <ul>
        <li>User Service → Port 5001</li>
        <li>Product Service → Port 5002</li>
        <li>Order Service → Port 5003</li>
        <li>Payment Service → Port 5004</li>
        <li>Notification Service → Port 5005</li>
    </ul>
    """

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "frontend-service"
    }

app.run(host="0.0.0.0", port=5000)