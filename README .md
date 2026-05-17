<div align="center">

# 🎓 EduPredict Pro
### AI-Powered Student Performance Prediction System

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)](https://plotly.com)
[![Accuracy](https://img.shields.io/badge/Model%20Accuracy-87%25-brightgreen?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

<br/>

> **Identify at-risk students before it's too late — powered by Machine Learning & Explainable AI.**

</div>

---

## 📌 Problem Statement

Educational institutions struggle to identify struggling students early. By the time poor academic performance is noticed, the window for meaningful intervention has often already closed — leading to dropouts, failures, and wasted potential.

> Traditional monitoring is **reactive**. EduPredict Pro is **proactive**.

---

## 💡 Solution

**EduPredict Pro** is an end-to-end AI-powered system that analyzes student academic data and predicts performance outcomes **in real time** — enabling educators to act early, with confidence and full transparency.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🤖 **ML Prediction Engine** | Random Forest classifier with **87% accuracy** on student outcome prediction |
| 📊 **Real-time Grade Prediction** | Instant predictions with confidence scores for every student |
| 🔍 **Explainable AI (XAI)** | Transparent, interpretable results that educators can understand and trust |
| 🚨 **Automated Alerts** | Smart notifications that flag high-risk students for timely educator intervention |
| 📈 **EDA & Visualizations** | Full exploratory data analysis with **18+ interactive charts**, heatmaps & statistics |
| ⚡ **Production REST API** | FastAPI backend ready for seamless institutional integration |
| 🎨 **Dark-Themed Dashboard** | Professional Streamlit frontend with an intuitive, polished UI |

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| **Language** | Python 3.9+ |
| **ML Model** | Random Forest · Scikit-learn |
| **Data Processing** | Pandas · NumPy |
| **Backend API** | FastAPI |
| **Frontend** | Streamlit |
| **Visualization** | Plotly · Matplotlib · Seaborn |
| **Auth / Config** | JSON-based user management |

</div>

---

## 📂 Project Structure

```
student-performance-system/
│
├── 📁 api/                     # FastAPI REST API backend
│   └── main.py                 # API routes & prediction endpoints
│
├── 📁 data/                    # Datasets (raw & processed)
│
├── 📁 frontend/                # Streamlit dashboard & UI
│
├── 📁 model/                   # ML model training & inference
│
├── 📁 root folder/             # Core app entry points & config
│
├── user.json                   # User session / profile data
├── users.json                  # User authentication records
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/bharathibr-123/student-performance-system.git
cd student-performance-system
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Start the FastAPI backend**
```bash
cd api
uvicorn main:app --reload
```

**4. Launch the Streamlit frontend**
```bash
cd frontend
streamlit run app.py
```

**5. Open your browser**
```
Frontend Dashboard  →  http://localhost:8501
API Documentation   →  http://localhost:8000/docs
```

---

## 📊 Model Performance

| Metric | Value |
|---|---|
| **Algorithm** | Random Forest Classifier |
| **Accuracy** | **87%** |
| **Output** | Grade prediction + confidence score |
| **Explainability** | Feature importance + XAI |

The model was trained with a full EDA pipeline — including correlation heatmaps, statistical distributions, and feature engineering — before deployment.

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `POST` | `/predict` | Predict student performance |
| `GET` | `/students` | Retrieve student records |
| `GET` | `/alerts` | Get high-risk student alerts |
| `GET` | `/docs` | Interactive Swagger UI documentation |

> Full API docs auto-generated at `http://localhost:8000/docs` when the server is running.

---

## 🧠 How It Works

```
Student Academic Data
        │
        ▼
  Data Preprocessing        ← Pandas + NumPy
        │
        ▼
  EDA & Feature Engineering ← 18+ Visualizations
        │
        ▼
  Random Forest Model       ← 87% Accuracy
        │
        ▼
  Prediction + Confidence Score
        │
        ├──────────────────────────┐
        ▼                          ▼
  Explainable AI (XAI)    Educator Alert System
                                   │
                                   ▼
                          FastAPI REST Endpoint
                                   │
                                   ▼
                        Streamlit Dark Dashboard
```

---

## 🎯 Use Cases

- 🏫 **Colleges & Universities** — Early detection of at-risk students across all departments
- 👩‍🏫 **Educators** — Data-driven insights instead of reactive observation
- 📋 **Academic Advisors** — Prioritize outreach using confidence-ranked risk scores
- 🔬 **EdTech Researchers** — Benchmark ML approaches for student outcome modeling

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 👤 Author

**Bharathi BR**

[![GitHub](https://img.shields.io/badge/GitHub-bharathibr--123-181717?style=flat-square&logo=github)](https://github.com/bharathibr-123)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### ⭐ If this project helped or inspired you, please give it a star!

*"Machine Learning is not just about models and accuracy — it's about solving problems that actually matter to people."*

**Made with ❤️ as a first ML project | There's a long road ahead — and this is just the beginning. 🚀**

</div>
