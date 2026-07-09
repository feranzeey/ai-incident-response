# AI Incident Response System

## Project Overview

This project is an automated AI-powered incident response system that monitors an application, detects issues, analyzes incidents, performs recovery actions, verifies system health, and generates incident reports.

---

# Architecture

Application
        │
        ▼
Prometheus + Loki + Promtail
        │
        ▼
Grafana
        │
        ▼
Alertmanager
        │
        ▼
FastAPI
        │
        ▼
AI Investigation
        │
        ▼
Automatic Recovery
        │
        ▼
Health Verification
        │
        ▼
Incident Report

---

# Features

- Flask Application
- Prometheus Monitoring
- Grafana Dashboards
- Loki Log Collection
- Promtail Log Shipping
- Alertmanager Alerts
- FastAPI Analysis Endpoint
- Automatic Incident Investigation
- Automatic Recovery
- Incident Report Generation

---

# Folder Structure

```
ai-incident-response
│
├── app
├── automation
├── docs
│   └── incidents
├── monitoring
├── screenshots
├── README.md
└── docker-compose.yml
```

---

# Installation

## Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

---

## Go into the project

```bash
cd ai-incident-response
```

---

## Start Docker

```bash
docker compose up -d
```

---

## Run the Flask application

```bash
python app.py
```

---

## Run FastAPI

```bash
uvicorn automation.api:app --reload
```

---

# Screenshots

## Flask Application

(Add screenshot here)

---

## Prometheus

(Add screenshot here)

---

## Grafana

(Add screenshot here)

---

## Loki

(Add screenshot here)

---

## Alertmanager

(Add screenshot here)

---

# Example Incident Workflow

High CPU

↓

Prometheus detects issue

↓

Grafana displays alert

↓

Alertmanager sends notification

↓

FastAPI starts analysis

↓

Metrics collected

↓

Logs collected

↓

AI determines root cause

↓

Automatic fix applied

↓

System verified

↓

Incident report generated

---

# Future Improvements

- OpenAI Integration
- Machine Learning Analysis
- Kubernetes Recovery
- Slack Notifications
- Email Alerts
- Predictive Monitoring

---

# Final Architecture

```
                Flask Application
                       │
                       ▼
          Prometheus + Loki + Promtail
                       │
                       ▼
                 Grafana Monitoring
                       │
              (Alert Triggered)
                       │
                       ▼
                 Alertmanager
                       │
        POST http://localhost:8000/analyze
                       │
                       ▼
              FastAPI Analysis API
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
  Read Metrics              Read Logs
 (Prometheus)                 (Loki)
          └────────────┬────────────┘
                       ▼
                 AI Investigation
                       ▼
               Choose Best Fix
        (Restart / Rollback / Scale)
                       ▼
                Verify the System
                       ▼
            Generate Incident Report
                       ▼
               Incident Resolved
```

---

# Author

Oluwaferanmi Dada