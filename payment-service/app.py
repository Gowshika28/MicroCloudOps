from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Payment Service Running"

@app.route("/payments")
def payments():
    return jsonify([
        {
            "payment_id": 201,
            "order_id": 101,
            "amount": 59999,
            "status": "Success"
        },
        {
            "payment_id": 202,
            "order_id": 102,
            "amount": 29999,
            "status": "Pending"
        }
    ])

@app.route("/process-payment", methods=["POST"])
def process_payment():
    return jsonify({
        "message": "Payment processed successfully",
        "status": "Success"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "payment-service"
    })

app.run(host="0.0.0.0", port=5004)