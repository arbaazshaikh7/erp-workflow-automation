# 📦 Intelligent ERP Workflow Automation System
### n8n | Python | SQL | Streamlit

---

## 🚀 Project Overview

This project simulates a **production-grade ERP analytics and automation system** designed to streamline data workflows, automate reporting, and provide real-time business insights.

It combines **workflow automation (n8n)**, **data processing (Python)**, and **structured storage (SQL)** into a fully automated pipeline.

---

## 🎯 Key Highlights

- ✅ End-to-end automated data pipeline  
- ✅ Real-time KPI monitoring system  
- ✅ ERP-style dataset with realistic business logic  
- ✅ Alert system for operational issues  
- ✅ Interactive dashboard for insights  

---

## 🏗️ Architecture

n8n Scheduler
      ↓
Data Ingestion (ERP Dataset)
      ↓
Python Processing (Pandas)
      ↓
SQLite Database
      ↓
 ┌───────────────
 ↓               ↓
Dashboard      Alert System
(Streamlit)    (Threshold-based)

---

## ⚙️ Tech Stack

- **Automation:** n8n  
- **Data Processing:** Python (Pandas, NumPy)  
- **Database:** SQLite  
- **Visualization:** Streamlit  
- **Data Source:** Synthetic ERP dataset  

---

## 📊 Dataset

This project uses a **synthetically generated ERP dataset** to simulate real-world business operations.

### 🔍 Dataset Features:
- Regional delivery performance variations  
- Supplier and warehouse relationships  
- Inventory distribution by product category  
- Seasonal spikes in demand and delays  
- Shipping cost correlated with order volume  

✅ Ensures:
- No confidential data exposure  
- Realistic business conditions  
- High-quality analytics capability  

---

## 📈 Key Features

### ✅ Automated Data Pipeline
- End-to-end workflow automation using n8n  
- Scheduled execution of data processing scripts  
- Fully reproducible pipeline  

---

### ✅ KPI Monitoring System
Tracks critical metrics such as:
- Total Orders  
- Delay Rate (%)  
- Average Delivery Time  
- Inventory Risk (low stock cases)  

---

### ✅ Business Insights
- Region-wise delivery performance  
- Product category demand analysis  
- Supplier efficiency evaluation  

---

### ✅ Anomaly Detection 🚨
- Identifies delayed shipments  
- Flags abnormal delivery times  
- Supports threshold-based alerting system  

---

### ✅ Interactive Dashboard 📊
- Built using Streamlit  
- Displays real-time KPIs and metrics  
- Visualizes operational trends  

---

## ⚡ How It Works

1. n8n triggers scheduled data pipeline  
2. Python script processes ERP data  
3. Data is stored in SQLite database  
4. KPIs and insights are generated  
5. Alerts are triggered for anomalies  
6. Dashboard displays updated data  

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt

Run data pipleine
python scripts/process_data.py

Launch dashboard:
streamlit run dashboard/app.py

---

## 🧠 Business Value

- Reduces manual reporting effort  
- Improves operational visibility  
- Enables faster decision-making  
- Demonstrates scalable automation system  

## 📸 Dashboard Preview

### ERP Analytics Dashboard

![Dashboard Preview](https://github.com/arbaazshaikh7/erp-workflow-automation/blob/main/dashboard.png)

---

⭐ If you found this project useful, consider giving it a star on GitHub.