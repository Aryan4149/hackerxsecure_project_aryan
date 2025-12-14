NetGuard-AI

Real-Time AI-Powered Cyber Threat Detection & Prevention System

Author: Aryan Yadav

1. Project Overview

NetGuard-AI is a real-time AI-driven cybersecurity system designed to detect, classify, and prevent network intrusions using machine learning.
The system analyzes network traffic data (CICIDS-style CSV features), identifies malicious activity, assesses severity, and provides actionable prevention decisions.

This project is built for hackathons and real-world demos, focusing on clarity, reliability, and fast deployment.

2. Key Features

Real-time network traffic analysis

AI-based attack classification using TabNet (PyTorch)

Supports batch CSV uploads (1 row to thousands)

Automatic severity scoring

Rule-based prevention decisions:

BLOCK

WARN

MONITOR

Human-readable prevention guidance

Web-based dashboard for easy interaction

Docker-based deployment for stability

3. Supported Attack Types

Benign Traffic

DoS Hulk

DDoS

FTP-Patator

SSH-Patator

Bot

PortScan

Infiltration

Web Attacks (SQL Injection, XSS, Brute Force)

Heartbleed

4. Tech Stack
Backend

Python 3.10

FastAPI

PyTorch

TabNet (pytorch-tabnet)

Scikit-Learn

Pandas, NumPy

Frontend

HTML

CSS

Vanilla JavaScript

Deployment

Docker

Railway (recommended for ML workloads)

5. Project Structure
NetGuard-AI/
│
├── api/
│   ├── main.py
│   ├── core/
│   │   ├── loader.py
│   │   ├── predict_engine.py
│   │   ├── prevention_engine.py
│   │   └── prevention_rules.py
│   └── routes/
│       └── upload.py
│
├── models/
│   ├── tabnet_full_model.zip
│   ├── scaler.pkl
│   ├── label_encoder.pkl
│   └── num_cols.pkl
│
├── web/
│   ├── static/
│   │   ├── style.css
│   │   └── script.js
│   └── templates/
│       └── home.html
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md

6. Model Details

Model: TabNetClassifier

Framework: PyTorch

Input: 77 numerical network traffic features

Output: Predicted attack label

Artifacts:

Trained TabNet model (ZIP)

Feature scaler

Label encoder

Feature order list

The model is loaded once at runtime and reused for predictions.

7. API Endpoints
Home
GET /


Returns the web dashboard.

Health Check
GET /health


Returns service and model load status.

CSV Upload & Prediction
POST /upload


Input: CSV file (no label column required)

Output: JSON containing detected attacks, severity, action, and prevention guide

8. Local Setup (Without Docker)
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --reload


Open browser:

http://127.0.0.1:8000

9. Docker Setup (Recommended)
Build Image
docker build -t netguard-ai .

Run Container
docker run -p 8000:8000 netguard-ai


Open:

http://localhost:8000

10. Deployment on Railway (Docker)

Push project to GitHub

Go to https://railway.app

New Project → Deploy from GitHub

Select repository

Railway auto-detects Dockerfile

Deploy

This setup avoids serverless limitations and supports heavy ML models.

11. Why Docker + Railway

No serverless cold-start issues

Stable PyTorch and TabNet execution

Full control over Python environment

Suitable for ML inference workloads

Hackathon-friendly and production-ready

12. Use Cases

Cybersecurity monitoring dashboards

Academic and research demonstrations

Hackathon and competition projects

Network security proof-of-concept systems

13. Disclaimer

This project is intended for educational and demonstration purposes.
It is not a replacement for enterprise-grade intrusion prevention systems.

14. Author

Aryan Yadav
AI / ML Developer
Hackathon Project Submission                                