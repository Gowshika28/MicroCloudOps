from flask import Flask
import requests

app = Flask(__name__)

services = [
    {
        "name": "User Service",
        "url": "http://user-service:5001/health",
        "port": "5001"
    },
    {
        "name": "Product Service",
        "url": "http://product-service:5002/health",
        "port": "5002"
    },
    {
        "name": "Order Service",
        "url": "http://order-service:5003/health",
        "port": "5003"
    },
    {
        "name": "Payment Service",
        "url": "http://payment-service:5004/health",
        "port": "5004"
    },
    {
        "name": "Notification Service",
        "url": "http://notification-service:5005/health",
        "port": "5005"
    }
]

@app.route("/")
def dashboard():

    cards = ""

    for service in services:

        try:
            response = requests.get(service["url"], timeout=2)

            if response.status_code == 200:
                status = "Healthy"
                color = "#22c55e"
            else:
                status = "Unhealthy"
                color = "#ef4444"

        except:
            status = "Down"
            color = "#ef4444"

        cards += f"""
        <div class="card">
            <h2>{service['name']}</h2>
            <p>Port: {service['port']}</p>
            <p style="color:{color}; font-weight:bold;">
                ● {status}
            </p>
        </div>
        """

    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>MicroCloudOps Dashboard</title>

    <style>

        body {{
            margin: 0;
            font-family: Arial;
            background: #020617;
            color: white;
        }}

        .header {{
            background: linear-gradient(90deg,#0f172a,#1d4ed8);
            padding: 30px;
            text-align: center;
        }}

        .header h1 {{
            color: #38bdf8;
            margin: 0;
            font-size: 40px;
        }}

        .container {{
            padding: 30px;
        }}

        .grid {{
            display: grid;
            grid-template-columns: repeat(3,1fr);
            gap: 20px;
        }}

        .card {{
            background: #0f172a;
            border-radius: 15px;
            padding: 20px;
            border: 1px solid #1e293b;
        }}

        h2 {{
            color: #38bdf8;
        }}

    </style>

</head>

<body>

    <div class="header">
        <h1>MicroCloudOps</h1>
        <p>Live DevOps Monitoring Dashboard</p>
    </div>

    <div class="container">

        <div class="grid">
            {cards}
        </div>

    </div>

</body>
</html>
"""

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "frontend-service"
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)