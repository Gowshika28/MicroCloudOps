from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>MicroCloudOps Dashboard</title>
        <style>
            body {
                font-family: Arial;
                background-color: #0f172a;
                color: white;
                padding: 40px;
            }

            h1 {
                color: #38bdf8;
            }

            .service {
                background: #1e293b;
                padding: 15px;
                margin: 10px 0;
                border-radius: 10px;
            }

            .healthy {
                color: #22c55e;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <h1>MicroCloudOps Dashboard</h1>

        <div class="service">
            User Service - Port 5001
            <div class="healthy">Healthy</div>
        </div>

        <div class="service">
            Product Service - Port 5002
            <div class="healthy">Healthy</div>
        </div>

        <div class="service">
            Order Service - Port 5003
            <div class="healthy">Healthy</div>
        </div>

        <div class="service">
            Payment Service - Port 5004
            <div class="healthy">Healthy</div>
        </div>

        <div class="service">
            Notification Service - Port 5005
            <div class="healthy">Healthy</div>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)