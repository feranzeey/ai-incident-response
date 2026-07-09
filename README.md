# AI-Powered Incident Response System

## Project Overview

The **AI-Powered Incident Response System** is an automated DevOps monitoring and incident response platform that detects infrastructure issues, collects system metrics and application logs, analyzes incidents, recommends recovery actions, verifies system health, and generates incident reports automatically.

The project integrates **Flask**, **Prometheus**, **Grafana**, **Loki**, **Promtail**, **Alertmanager**, and **FastAPI** to simulate a modern Site Reliability Engineering (SRE) and DevOps workflow.

---

# Features

* Real-time application monitoring
* Metrics collection using Prometheus
* Log aggregation using Loki
* Log shipping with Promtail
* Grafana dashboards for visualization
* Alertmanager integration for automated alerts
* FastAPI endpoint for incident analysis
* Automatic log retrieval from Loki
* Automatic metric retrieval from Prometheus
* AI-inspired incident investigation logic
* Automated recovery decision engine
* Incident verification after recovery
* Automatic incident report generation
* Modular and extensible project structure

---

# Technology Stack

* Python
* Flask
* FastAPI
* Docker & Docker Compose
* Prometheus
* Grafana
* Loki
* Promtail
* Alertmanager
* Requests
* Git & GitHub

---

# Architecture Diagram

```text
                   Flask Application
                           │
                           ▼
              Prometheus + Loki + Promtail
                           │
                           ▼
                  Grafana Monitoring
                           │
                  Alert Triggered
                           │
                           ▼
                    Alertmanager
                           │
          POST http://localhost:8000/analyze
                           │
                           ▼
                 FastAPI Analysis API
                           │
          ┌────────────────┴────────────────┐
          ▼                                 ▼
   Read Metrics                     Read Logs
 (Prometheus API)                  (Loki API)
          └────────────────┬────────────────┘
                           ▼
                  AI Investigation
                           ▼
                 Recovery Decision
         Restart • Rollback • Scale • Clear Cache
                           ▼
                 Verify System Health
                           ▼
              Generate Incident Report
                           ▼
                  Incident Resolved
```

---

# Folder Structure

```text
ai-incident-response/
│
├── app/
│   └── Flask application
│
├── automation/
│   ├── api.py
│   ├── read_metrics.py
│   ├── read_loki.py
│   ├── investigate.py
│   ├── fix.py
│   ├── verify.py
│   └── postmortem.py
│
├── monitoring/
│   ├── prometheus.yml
│   ├── promtail.yml
│   └── alertmanager.yml
│
├── docs/
│   └── incidents/
│       └── report.md
│
├── logs/
│
├── screenshots/
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/feranzeey/ai-incident-response.git
```

## 2. Navigate to the Project

```bash
cd ai-incident-response
```

## 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## 4. Start All Services

```bash
docker compose up -d
```

This starts:

* Flask Application
* Prometheus
* Grafana
* Loki
* Promtail
* Alertmanager

---

# Usage

## Run the Flask Application

```bash
python app.py
```

---

## Run the FastAPI Service

```bash
uvicorn automation.api:app --reload
```

---

## Read Metrics from Prometheus

```bash
python automation/read_metrics.py
```

---

## Read Logs from Loki

```bash
python automation/read_loki.py
```

---

## Generate an Incident Report

```bash
python automation/postmortem.py
```

The report will be generated in:

```text
docs/incidents/report.md
```

---

# Project Components

| Component         | Purpose                    |
| ----------------- | -------------------------- |
| Flask             | Sample application         |
| Prometheus        | Collects system metrics    |
| Grafana           | Monitoring dashboards      |
| Loki              | Stores application logs    |
| Promtail          | Sends logs to Loki         |
| Alertmanager      | Handles alerts             |
| FastAPI           | Incident analysis API      |
| Python Automation | Investigation and recovery |

---

# Screenshots

Add screenshots to the `screenshots/` folder and update the paths below.

## Flask Application

```
screenshots/flask.png
```

---

## Prometheus Dashboard

```
screenshots/prometheus.png
```

---

## Grafana Dashboard

```
screenshots/grafana.png
```

---

## Loki

```
screenshots/loki.png
```

---

## Alertmanager

```
screenshots/alertmanager.png
```

---

## FastAPI Documentation

```
screenshots/fastapi.png
```

---

# Example Incident Workflow

```text
Application Running
        │
        ▼
Prometheus detects high CPU
        │
        ▼
Grafana visualizes the issue
        │
        ▼
Alertmanager sends an alert
        │
        ▼
FastAPI receives POST /analyze
        │
        ▼
Python collects:
 • CPU Metrics
 • Memory Metrics
 • Logs from Loki
        │
        ▼
AI Investigation
        │
        ▼
Recovery Decision
        │
        ├── Restart Service
        ├── Scale Containers
        ├── Rollback Deployment
        └── Clear Cache
        │
        ▼
Verify System Health
        │
        ▼
Generate Incident Report
        │
        ▼
Incident Closed
```

---

# Sample Incident Report

```text
Root Cause:
High CPU Usage

Confidence:
95%

Recommended Action:
Restart Service

Status:
Resolved
```

---

# Future Improvements

* OpenAI-powered root cause analysis
* Kubernetes deployment automation
* Automatic rollback strategy
* Slack notifications
* Microsoft Teams integration
* Email alerting
* Predictive anomaly detection
* Machine Learning models
* Historical incident database
* Executive dashboards
* Multi-service monitoring
* Cloud deployment (AWS/Azure)

---

# Learning Outcomes

This project demonstrates practical experience with:

* DevOps Monitoring
* Observability
* Site Reliability Engineering (SRE)
* Incident Management
* Docker
* Python Automation
* FastAPI
* Prometheus
* Grafana
* Loki
* Alertmanager
* Log Management
* Monitoring Best Practices

---

# Author

**Oluwaferanmi Dada**

GitHub: https://github.com/feranzeey

---
