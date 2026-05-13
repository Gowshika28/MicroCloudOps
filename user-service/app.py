from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "User Service",
        "platform": "MicroCloudOps E-Commerce",
        "status": "running",
        "description": "Handles user-related operations"
    })

@app.route("/health")
def health():
    return jsonify({
        "service": "user-service",
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)