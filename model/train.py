import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

np.random.seed(42)
n = 500

attendance       = np.random.randint(40, 100, n)
assignment_avg   = np.random.randint(30, 100, n)
midterm_score    = np.random.randint(30, 100, n)
quiz_avg         = np.random.randint(30, 100, n)
late_submissions = np.random.randint(0, 15, n)
study_hours      = np.random.randint(0, 40, n)

score = (
    attendance       * 0.25 +
    assignment_avg   * 0.20 +
    midterm_score    * 0.30 +
    quiz_avg         * 0.15 +
    (15 - late_submissions) * 0.5 +
    np.clip(study_hours, 0, 20) * 0.5
)

def score_to_grade(s):
    if s >= 85:   return 'A'
    elif s >= 72: return 'B'
    elif s >= 60: return 'C'
    elif s >= 50: return 'D'
    else:         return 'F'

grades = [score_to_grade(s) for s in score]

df = pd.DataFrame({
    'attendance':       attendance,
    'assignment_avg':   assignment_avg,
    'midterm_score':    midterm_score,
    'quiz_avg':         quiz_avg,
    'late_submissions': late_submissions,
    'study_hours':      study_hours,
    'grade':            grades
})

os.makedirs('data',  exist_ok=True)
os.makedirs('model', exist_ok=True)
df.to_csv('data/students.csv', index=False)
print(f"Dataset saved — {n} records")

X = df.drop('grade', axis=1)
y = df['grade']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc  = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_sc, y_train)

y_pred = model.predict(X_test_sc)
acc    = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {acc*100:.2f}%")
print("\nDetailed Report:")
print(classification_report(y_test, y_pred))

joblib.dump(model,  'model/rf_model.pkl')
joblib.dump(scaler, 'model/scaler.pkl')
print("Model and scaler saved successfully!")