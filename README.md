# 🚀 DevOps Portfolio – Production Auto Deploy Stack

This project demonstrates a real-world DevOps production workflow built from scratch on a VPS.

It includes:

- 🐳 Docker & Docker Compose
- 🌐 Nginx Reverse Proxy
- 🔁 GitHub Webhook CI/CD (Auto Deploy)
- 🖥 Ubuntu VPS Deployment
- 🔐 SSH & Server Hardening
- 📊 (Upcoming) Monitoring with Prometheus & Grafana
- ⚙ (Upcoming) CI/CD using GitHub Actions

---

## 🌍 Live Architecture



---

## 🐳 Tech Stack

| Component | Description |
|-----------|------------|
| Ubuntu VPS | Production server |
| Docker | Containerization |
| Docker Compose | Multi-service orchestration |
| Nginx | Reverse proxy |
| Flask | Portfolio application |
| GitHub | Source control |
| GitHub Webhook | Auto deploy trigger |

---

## 🔁 CI/CD – Auto Deployment System

This project uses GitHub Webhooks to trigger automatic deployment.

When code is pushed to the `main` branch:

1. GitHub sends a POST request to VPS
2. Webhook service receives trigger
3. Server executes:
   - `git pull`
   - `docker compose down`
   - `docker compose up -d --build`
4. Application updates instantly

### 📸 Automation Proof

![Auto Deploy Proof](images/auto-deploy-proof.png)

---

## 🧠 What I Built

- Full VPS setup from scratch
- SSH configuration & user management
- Dockerized Flask application
- Reverse proxy configuration with Nginx
- Manual CI/CD system using webhook service
- Multi-container management with Docker Compose
- Real deployment pipeline simulation

---

## 📊 Upcoming Improvements

### ✅ GitHub Actions CI/CD (Professional Pipeline)
- Build Docker image automatically
- Deploy via secure SSH
- Zero manual trigger

### ✅ Monitoring Stack
- Prometheus
- Grafana Dashboard
- Node Exporter
- Container monitoring

### ✅ HTTPS Production Setup
- Domain configuration
- Let's Encrypt SSL
- Secure reverse proxy

---

## 🎯 Learning Objectives

This project simulates a real DevOps production environment including:

- Infrastructure provisioning
- Deployment automation
- Container orchestration
- Reverse proxy configuration
- CI/CD pipeline fundamentals
- System troubleshooting

---

## 📬 Contact

Feel free to connect for collaboration or opportunities.

DevOps Engineer in Progress 🚀
