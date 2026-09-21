# Diabetes Prediction

## Synopsis
This project uses machine learning to predict whether a person is likely to have diabetes using health-related features such as glucose level, BMI, age, blood pressure, and other measurements.

## Objectives
- Understand the diabetes dataset.
- Analyze different health-related features.
- Clean and prepare the data.
- Train a machine learning model.
- Predict diabetes outcomes.
- Measure model performance.

## Tools
Python, Pandas, Matplotlib, Scikit-learn

## Dataset Features
- pregnancies
- glucose
- blood_pressure
- skin_thickness
- insulin
- bmi
- diabetes_pedigree
- age
- outcome

Target:
- 0 = No Diabetes
- 1 = Diabetes

## Data Preparation
- Loaded the CSV dataset using Pandas.
- Checked for missing values.
- Filled missing numerical values with median values.
- Split the data into training and testing sets.
- Standardized features using StandardScaler.

## Machine Learning Algorithm
Logistic Regression is used for binary classification.

## Evaluation
The program calculates:
- Accuracy
- Classification report
- Confusion matrix

It also creates a scatter plot showing glucose level versus BMI.

## How to Run
1. Install Python.
2. Open a terminal in this project folder.
3. Install dependencies:
   pip install -r requirements.txt
4. Run:
   python diabetes_prediction.py

## Important Note
This is an educational machine-learning project using a classroom dataset. It is not a medical diagnostic tool and should not be used for clinical decisions.
