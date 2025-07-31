# 🚀 CodePulse: Real-Time Developer Burnout Early Warning System

**CodePulse** is a full-stack observability and DevOps project that simulates real-time developer activity logs, monitors emotional health, and visualizes patterns using the ELK stack (Elasticsearch, Kibana) with containerized services using Docker.

---

## 📌 Table of Contents

- 📘 [Project Overview](#project-overview)  
- 🧱 [Architecture](#architecture)  
- 🛠️ [Tech Stack](#tech-stack)  
- ⚙️ [How It Works](#how-it-works)  
- 🚀 [Getting Started](#getting-started)  
- 📊 [Observability Dashboards](#observability-dashboards)  
- 💡 [Use Cases](#use-cases)  
- 📂 [Project Structure](#project-structure)  
- 🧪 [Future Enhancements](#future-enhancements)  

---

## 📘 Project Overview

Developer burnout is a critical but often ignored issue in the software industry. CodePulse is a simulated DevOps solution that generates real-time logs mimicking developer behavior (emotions, productivity, context switches), sends them to Elasticsearch, and visualizes these metrics in Kibana dashboards for actionable insights.

---

## 🧱 Architecture

+----------------------+ POST +----------------------+ PUSH +----------------------+
| simulate_logs.py | -------> | FastAPI Monitor | -------> | Elasticsearch |
| (Log Generator) | | (Receives + Filters) | | (Search & Storage) |
+----------------------+ +----------------------+ +----------+-----------+
| Visualization via |
| Kibana UI |
+----------------------+


---

## 🛠️ Tech Stack

| Layer            | Tool/Service           |
|------------------|------------------------|
| 🚀 Simulation     | Python (`simulate_logs.py`) |
| 🧠 Monitoring      | FastAPI                |
| 📦 Containerization | Docker, Docker Compose |
| 🔍 Search & Storage | Elasticsearch         |
| 📈 Visualization   | Kibana                |
| 🔗 GitHub Webhooks | (Future integration)  |

---

## ⚙️ How It Works

- **Log Simulation**  
  `simulate_logs.py` generates logs every second with:
  - `timestamp`
  - `developer_name`
  - `emotion`
  - `mood_level`

- **Monitor Service (FastAPI)**  
  Captures incoming logs and forwards them to Elasticsearch.

- **Elasticsearch**  
  Stores and indexes logs for real-time searching.

- **Kibana**  
  Visualizes developer behavior through:
  - Pie charts
  - Bar graphs
  - Line charts

---

## 🚀 Getting Started

### ✅ Prerequisites

- Docker & Docker Compose
- Python 3.11+
- Git

### 📥 Clone the Repo
git clone https://github.com/your-username/codepulse-devops.git
cd codepulse-devops

### 🐳 Start the Containers
docker-compose up --build

🐍 Start Log Simulation

In a separate terminal:
cd monitor
python simulate_logs.py

You should now see logs flowing into Elasticsearch.


📊 Observability Dashboards (Kibana)
Open Kibana at: http://localhost:5601

Create a Data View (e.g., codepulse-*)

Use the Discover tab to see logs in real time

Create the following visualizations:

Developer Emotion Pie Chart

Burnout Bar Chart (Y-axis: mood_level)

Health Line Chart (X-axis: @timestamp)

Combine visualizations into a Kibana Dashboard

💡 Use Cases
Real-time monitoring of developer emotional health

Full-stack observability showcase with ELK stack

Resume-worthy DevOps portfolio project

GitHub-triggered log ingestion (future enhancement)

📂 Project Structure

codepulse-devops/
│
├── docker-compose.yml          # Orchestrates services
│
├── monitor/
│   ├── app/
│   │   ├── main.py             # FastAPI entrypoint
│   │   ├── elastic_client.py   # Push logs to Elasticsearch
│   │   ├── utils.py            # Helper functions
│   │   └── github_webhook_handler.py  # GitHub event handling (future)
│   ├── simulate_logs.py        # Developer log simulation
│   ├── requirements.txt        # Python dependencies
│   └── Dockerfile              # Docker setup for FastAPI app


🧪 Future Enhancements
✅ GitHub webhook integration to track PRs, issues, and commits

✅ Slack/Discord alerts for burnout detection

✅ ML model to predict emotional health

✅ Infrastructure observability via Prometheus + Grafana
