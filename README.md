# AI Incident Response System

A DevOps project that demonstrates automated incident detection, monitoring, system health checks, application recovery, and incident reporting using Docker, Flask, FastAPI, Prometheus, and Grafana.

---

## Overview

The AI Incident Response System is designed to automate key incident response tasks commonly performed by DevOps and Site Reliability Engineering (SRE) teams.

The project monitors an application, collects metrics, performs health checks, automates recovery actions, and generates incident reports to reduce manual intervention and improve system reliability.

---

## Features

- Dockerized Flask application
- FastAPI automation service
- Prometheus metrics collection
- Grafana monitoring and alerting
- Application health checks
- System resource monitoring
- Log collection
- Automated application restart
- Incident report generation
- Modular project structure

---

## Technology Stack

- Python 3.12
- Flask
- FastAPI
- Docker
- Docker Compose
- Prometheus
- Grafana
- Requests
- psutil

---

## Project Structure

```
ai-incident-response/
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── automation/
│   ├── analyze.py
│   ├── health.py
│   ├── logs.txt
│   ├── main.py
│   ├── read_logs.py
│   ├── restart.py
│   └── system.py
│
├── monitoring/
│   └── prometheus.yml
│
├── reports/
│   └── report.md
│
├── screenshots/
│
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

## System Workflow

```
Flask Application
        │
        ▼
Prometheus
        │
        ▼
Grafana
        │
        ▼
Automation Service
        │
        ▼
Collect Logs
        │
        ▼
Check System Health
        │
        ▼
Restart Application
        │
        ▼
Health Verification
        │
        ▼
Generate Incident Report
```

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/feranzeey/ai-incident-response.git
```

```bash
cd ai-incident-response
```

### Start the application

```bash
docker compose up -d
```

### Verify running containers

```bash
docker ps
```

---

## Application URLs

| Service | URL |
|---------|-----|
| Flask Application | http://localhost:5000 |
| Metrics Endpoint | http://localhost:5000/metrics |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |
| Automation Service | http://localhost:8000 |

---

## Monitoring

Prometheus collects application metrics from the Flask application.

Grafana provides dashboards and alerting for monitoring application health and system performance.

The monitoring setup includes:

- Application availability
- Request metrics
- CPU monitoring
- Memory monitoring
- Health status

---

## Automation

The automation service performs the following tasks:

- Reads application logs
- Collects system information
- Performs health checks
- Restarts the application when required
- Generates incident reports

---

## Incident Response Process

1. Monitor application metrics.
2. Detect abnormal system behavior.
3. Collect logs and system information.
4. Perform health checks.
5. Restart the application if required.
6. Verify recovery.
7. Generate an incident report.

---

## Sample Incident Report

The generated report contains:

- Incident time
- Problem summary
- Evidence collected
- Root cause
- Resolution steps
- Health check results
- Recovery status
- Recommended next steps

---

## Screenshots

The project includes screenshots demonstrating:

- Flask application
- Prometheus metrics
- Automation service
- Prometheus targets
- Grafana alert configuration
- Incident report
- System architecture

---

## Future Improvements

Planned enhancements include:

- Alertmanager integration
- Email notifications
- Slack notifications
- Microsoft Teams notifications
- Automatic rollback
- Kubernetes deployment
- Centralized log management
- Predictive anomaly detection
- Cloud deployment on AWS

---

## Skills Demonstrated

This project demonstrates practical experience with:

- DevOps
- Docker
- Docker Compose
- Monitoring
- Observability
- Incident Response
- FastAPI
- Flask
- Prometheus
- Grafana
- Python Automation
- System Health Monitoring

---

## Author

**Feranmi Dada**

GitHub: https://github.com/feranzeey

LinkedIn: https://www.linkedin.com/in/feranmi-dada/

---

## License

This project is intended for learning, demonstration, and portfolio purposes.