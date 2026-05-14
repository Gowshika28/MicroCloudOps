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