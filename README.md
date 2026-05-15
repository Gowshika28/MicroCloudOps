# MicroCloudOps

MicroCloudOps is a microservices-based DevOps project built using Flask, Docker, Docker Compose, GitHub, and monitoring tools.

## Current Status

- Multiple Flask microservices created
- Dockerfiles added for each service
- Docker Compose setup added
- Health check endpoints added
- Prometheus monitoring configuration started
- Project version controlled using Git and GitHub

## Services

- Frontend Service - 5000
- User Service - 5001
- Product Service - 5002
- Order Service - 5003
- Payment Service - 5004
- Notification Service - 5005

## Health Check Endpoints

- `/health` endpoint added for service status checking

## Pending Enhancements

- Frontend dashboard
- Grafana dashboard
- Real unhealthy condition logic
- API Gateway
- Centralized logging
- Cloud deployment
- CI/CD pipeline
## Architecture

MicroCloudOps follows a microservices architecture where each service runs independently inside its own Docker container.

### Services

| Service | Purpose | Port |
|---------|---------|------|
| Frontend Service | Dashboard UI | 5000 |
| User Service | User management | 5001 |
| Product Service | Product management | 5002 |
| Order Service | Order processing | 5003 |
| Payment Service | Payment handling | 5004 |
| Notification Service | Notifications and alerts | 5005 |

## Monitoring Stack

- Prometheus for monitoring
- Grafana for visualization
- Health endpoints for service monitoring

## DevOps Features

- Dockerized microservices
- Docker Compose orchestration
- GitHub version control
- Monitoring configuration
- Health check endpoints
## API Gateway

The API Gateway acts as a single entry point for accessing backend microservices.

### Gateway Routes

- `/product` → Product Service
- `/order` → Order Service
- `/payment` → Payment Service
- `/notification` → Notification Service
- `/health` → API Gateway health check

## Database Integration

- Product Service uses SQLite for product data
- Order Service uses SQLite for order data

## Frontend Dashboard

The frontend dashboard displays live service health status for:

- API Gateway
- User Service
- Product Service
- Order Service
- Payment Service
- Notification Service
# MicroCloudOps

MicroCloudOps is a microservices-based DevOps platform built using Flask, Docker, and monitoring tools.

## Features

- Microservices Architecture
- API Gateway
- Service-to-Service Communication
- Health Monitoring Dashboard
- SQLite Databases
- Prometheus Metrics
- Docker & Docker Compose Setup
- GitHub CI/CD Workflow

---

## Services

| Service | Port | Description |
|---|---|---|
| Frontend Service | 5000 | Monitoring Dashboard |
| API Gateway | 8000 | Central API Routing |
| User Service | 5001 | User Management |
| Product Service | 5002 | Product Management |
| Order Service | 5003 | Order Processing |
| Payment Service | 5004 | Payment Handling |
| Notification Service | 5005 | Notifications |

---

## Architecture

Frontend Dashboard → API Gateway → Microservices

Microservices communicate internally using REST APIs.

---

## Tech Stack

- Python Flask
- SQLite
- Docker
- Docker Compose
- Prometheus
- GitHub Actions

---

## Run Locally

```bash
python app.py