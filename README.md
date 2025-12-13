🚨 NetGuard-AI
AI-Powered Network Intrusion Detection & Prevention System

Author: Aryan Yadav
Category: Cybersecurity • Artificial Intelligence • Deep Learning

📌 Project Summary

NetGuard-AI is a real-time AI-powered cybersecurity system designed to detect, classify, and prevent malicious network activities.
The system analyzes network traffic data and automatically determines the attack type, severity level, and appropriate prevention action using a deep learning model.

This project is built specifically for hackathons, cybersecurity demos, and AI research showcases.

🎯 Problem Statement

Modern networks generate massive volumes of traffic, making manual threat monitoring ineffective.
Traditional rule-based systems fail to adapt to evolving attack patterns.

NetGuard-AI solves this problem by using AI-driven intelligence to automatically detect intrusions and recommend mitigation strategies in real time.

🧠 Solution Overview

NetGuard-AI uses a TabNet deep learning model trained on network traffic features to:

Detect malicious activity

Classify attack types

Calculate severity using model confidence

Decide prevention action:

BLOCK

WARN

MONITOR

Display clear, human-readable prevention guidance

🚀 Key Features

AI-based Network Intrusion Detection System (NIDS)

Batch CSV traffic analysis (CIC-IDS style features)

Deep Learning model (TabNet – PyTorch)

Severity scoring based on prediction confidence

Automatic prevention decision engine

Interactive web dashboard

FastAPI backend

Vercel-ready deployment

🧪 Supported Attack Classes

Benign

DoS Hulk

DDoS

FTP-Patator

SSH-Patator

Web Attacks (SQL Injection, XSS, Brute Force)

Bot

Infiltration

Heartbleed

🧠 AI / ML Details

Model: TabNetClassifier (PyTorch TabNet)

Input: 77 numeric network traffic features

Output: Attack label + confidence score

Severity Logic: Derived from model probability

Model Artifacts

Stored in the models/ directory:

tabnet_full_model.zip

scaler.pkl

label_encoder.pkl

num_cols.pkl

🏗️ Project Structure
NetGuard-AI/
│
├── api/                # FastAPI backend
├── web/                # Frontend dashboard (HTML, CSS, JS)
├── models/             # Trained model artifacts
│
├── notebooks/          # Training & experimentation notebooks
│   └── cyber.ipynb
│
├── requirements.txt
├── vercel.json
├── .gitignore
└── README.md

⚙️ Technology Stack
Backend

FastAPI

PyTorch

PyTorch-TabNet

Scikit-learn

Pandas, NumPy

Frontend

HTML

CSS (Custom dark cybersecurity dashboard)

Vanilla JavaScript

Deployment

GitHub

Vercel (Serverless)

🔄 System Workflow

User uploads a network traffic CSV file

Backend preprocesses the data

AI model predicts attack type and confidence

Severity score is calculated

Prevention decision is generated

Results and mitigation guidance are displayed on the dashboard

🖥️ Running the Project Locally
1️⃣ Create virtual environment
python -m venv hack1env
source hack1env/bin/activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Start FastAPI server
uvicorn api.main:app --reload


Open in browser:

http://127.0.0.1:8000

☁️ Deployment Notes (Vercel)

FastAPI runs as a serverless function

Frontend is served using Jinja2 templates

Notebooks are included for reference but not executed in production

Only trained model artifacts are used during deployment

📓 Notebooks

notebooks/cyber.ipynb includes:

Data exploration

Feature engineering

Model training

Evaluation experiments

This ensures reproducibility and transparency.

🧩 Use Cases

Hackathon projects

Cybersecurity demonstrations

Academic AI/ML projects

Network intrusion research

AI-based SOC tools

👨‍💻 Author

Aryan Yadav
AI / ML Developer
Cybersecurity & Deep Learning Enthusiast

🏁 One-Line Hackathon Pitch

NetGuard-AI is an AI-powered network intrusion detection and prevention system that analyzes network traffic to detect cyber attacks and automatically recommend mitigation actions in real time.