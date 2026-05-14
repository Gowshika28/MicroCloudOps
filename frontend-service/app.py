from flask import Flask

app = Flask(__name__)

@app.route("/")
def dashboard():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>MicroCloudOps Dashboard</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #020617;
            color: white;
        }

        .header {
            background: linear-gradient(90deg, #0f172a, #1e40af);
            padding: 30px;
            text-align: center;
        }

        .header h1 {
            margin: 0;
            font-size: 42px;
            color: #38bdf8;
        }

        .header p {
            color: #cbd5e1;
            font-size: 18px;
        }

        .container {
            padding: 30px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }

        .card {
            background: #0f172a;
            border: 1px solid #1e293b;
            border-radius: 16px;
            padding: 22px;
            box-shadow: 0 0 20px rgba(56,189,248,0.08);
        }

        .card h2 {
            color: #38bdf8;
            margin-top: 0;
        }

        .status {
            color: #22c55e;
            font-weight: bold;
        }

        .tag {
            display: inline-block;
            background: #1e293b;
            color: #93c5fd;
            padding: 6px 10px;
            border-radius: 20px;
            margin-top: 8px;
        }

        .section-title {
            margin-top: 40px;
            color: #facc15;
        }

        .monitoring {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin-top: 20px;
        }

        .footer {
            text-align: center;
            padding: 20px;
            color: #94a3b8;
        }
    </style>
</head>

<body>

    <div class="header">
        <h1>MicroCloudOps</h1>
        <p>Intelligent DevOps Automation Platform for Microservices Monitoring</p>
    </div>

    <div class="container">

        <h2 class="section-title">Microservices Status</h2>

        <div class="cards">
            <div class="card">
                <h2>Frontend Service</h2>
                <p>Dashboard UI</p>
                <p>Port: 5000</p>
                <p class="status">● Healthy</p>
                <span class="tag">UI Layer</span>
            </div>

            <div class="card">
                <h2>User Service</h2>
                <p>User management service</p>
                <p>Port: 5001</p>
                <p class="status">● Healthy</p>
                <span class="tag">Backend API</span>
            </div>

            <div class="card">
                <h2>Product Service</h2>
                <p>Product database and product APIs</p>
                <p>Port: 5002</p>
                <p class="status">● Healthy</p>
                <span class="tag">SQLite DB</span>
            </div>

            <div class="card">
                <h2>Order Service</h2>
                <p>Creates orders by calling Product Service</p>
                <p>Port: 5003</p>
                <p class="status">● Healthy</p>
                <span class="tag">Service Communication</span>
            </div>

            <div class="card">
                <h2>Payment Service</h2>
                <p>Payment processing flow</p>
                <p>Port: 5004</p>
                <p class="status">● Healthy</p>
                <span class="tag">Transaction Layer</span>
            </div>

            <div class="card">
                <h2>Notification Service</h2>
                <p>Sends payment notifications</p>
                <p>Port: 5005</p>
                <p class="status">● Healthy</p>
                <span class="tag">Alert System</span>
            </div>
        </div>

        <h2 class="section-title">Monitoring Stack</h2>

        <div class="monitoring">
            <div class="card">
                <h2>Prometheus</h2>
                <p>Collects service metrics and monitors health endpoints.</p>
                <p>Port: 9090</p>
                <span class="tag">Metrics Monitoring</span>
            </div>

            <div class="card">
                <h2>Grafana</h2>
                <p>Visualizes metrics using dashboards and graphs.</p>
                <p>Port: 3000</p>
                <span class="tag">Dashboard Visualization</span>
            </div>
        </div>

        <h2 class="section-title">DevOps Features</h2>

        <div class="cards">
            <div class="card">
                <h2>Docker</h2>
                <p>Each service runs inside its own container.</p>
            </div>

            <div class="card">
                <h2>Docker Compose</h2>
                <p>Runs all microservices together using one command.</p>
            </div>

            <div class="card">
                <h2>GitHub CI/CD</h2>
                <p>Project is version controlled and ready for pipeline automation.</p>
            </div>
        </div>

    </div>

    <div class="footer">
        MicroCloudOps © 2026 | DevOps + Cloud + Microservices Project
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