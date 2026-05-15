# MicroCloudOps Architecture

```text
User
 |
 v
Frontend Dashboard (5000)
 |
 v
API Gateway (8000)
 |
 +--> User Service (5001)
 +--> Product Service (5002) --> SQLite DB
 +--> Order Service (5003) --> SQLite DB
 +--> Payment Service (5004)
 +--> Notification Service (5005)

Monitoring:
Prometheus --> /metrics endpoints
Grafana --> Dashboards