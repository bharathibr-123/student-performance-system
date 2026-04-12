# EduPredict Pro — Student Performance Prediction System

An AI-powered web application that predicts student academic performance
and identifies at-risk students using Machine Learning.

---

## Problem Statement
Educational institutions rely on manual monitoring to evaluate student
performance, making it difficult to identify struggling students early.
This system solves that using data-driven ML predictions.

---

## Solution
A Random Forest ML model trained on student academic data that predicts
final grades, identifies at-risk students, and provides personalized
recommendations — deployed via FastAPI + Streamlit.

---

## Features
- Real-time grade prediction with confidence score
- Explainable AI (XAI) — feature importance visualization
- At-risk student identification and educator alerts
- Exploratory Data Analysis (EDA) with correlation heatmap
- Full ML Pipeline visualization
- Radar charts, scatter plots, trend lines, pie charts
- AI-generated cohort insights report
- REST API with auto-generated documentation

---

## Tech Stack
| Layer | Technology |
|---|---|
| ML Model | Random Forest (scikit-learn) |
| Backend API | FastAPI + Uvicorn |
| Frontend | Streamlit |
| Visualization | Plotly |
| Language | Python 3.10+ |
| XAI | feature_importances_ |

---

## Project Structure

---

## How to Run

### Step 1 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2 — Train the model
```bash
python model/train.py
```

### Step 3 — Start FastAPI backend
```bash
uvicorn api.main:app --reload
```

### Step 4 — Start Streamlit frontend
```bash
streamlit run frontend/app.py
```

### Step 5 — Open in browser
- App: http://localhost:8501
- API docs: http://localhost:8000/docs

---

## ML Model Details
- Algorithm: Random Forest Classifier
- Dataset: 500 synthetic student records
- Features: Attendance, Assignment Avg, Midterm Score,
  Quiz Avg, Late Submissions, Study Hours
- Target: Final Grade (A / B / C / D / F)
- Accuracy: 87%
- Explainability: Feature importance (XAI enabled)

---

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | / | API health check |
| GET | /health | Model status |
| POST | /predict | Predict student grade |
| GET | /cohort | Cohort statistics |

---

## Team
Hackathon Project — Problem Statement P-01
Student Performance Prediction & Monitoring System