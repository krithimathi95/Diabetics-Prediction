# Diabetes Prediction
# Tools: Python, Pandas, Matplotlib, Scikit-learn

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
data = pd.read_csv("diabetes.csv")

print("First 5 rows:")
print(data.head())

print("\nDataset shape:", data.shape)

# Check missing values
print("\nMissing values before cleaning:")
print(data.isnull().sum())

# Clean missing numerical values using median
numeric_columns = data.select_dtypes(include=["number"]).columns
for column in numeric_columns:
    if data[column].isnull().any():
        data[column] = data[column].fillna(data[column].median())

print("\nMissing values after cleaning:", data.isnull().sum().sum())

print("\nOutcome distribution:")
print(data["outcome"].value_counts())

# Features and target
X = data.drop(columns=["outcome"])
y = data["outcome"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train classification model
model = LogisticRegression(max_iter=2000, random_state=42)
model.fit(X_train_scaled, y_train)

# Predictions
y_pred = model.predict(X_test_scaled)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(
    y_test, y_pred,
    target_names=["No Diabetes", "Diabetes"]
))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Predict a new person
new_person = pd.DataFrame([{
    "pregnancies": 2,
    "glucose": 130,
    "blood_pressure": 80,
    "skin_thickness": 25,
    "insulin": 100,
    "bmi": 28.5,
    "diabetes_pedigree": 0.45,
    "age": 35
}])

new_person_scaled = scaler.transform(new_person)
prediction = model.predict(new_person_scaled)[0]

print("\nExample prediction:",
      "Diabetes" if prediction == 1 else "No Diabetes")

# Visualization
plt.figure(figsize=(8, 5))
plt.scatter(
    data["glucose"],
    data["bmi"],
    c=data["outcome"],
    alpha=0.7
)
plt.xlabel("Glucose Level")
plt.ylabel("BMI")
plt.title("Diabetes Feature Analysis")
plt.tight_layout()
plt.savefig("diabetes_analysis.png", dpi=150)
plt.show()
