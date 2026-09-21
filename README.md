# Diabetics-Prediction
Diabetes Prediction is a machine learning project that predicts whether a person is likely to have diabetes based on health-related measurements.
# Diabetes Prediction Using Machine Learning

## Project Description

Diabetes Prediction is a machine learning project that predicts whether a person is likely to have diabetes based on health-related measurements.

The project uses **Logistic Regression**, a supervised machine learning classification algorithm, to classify patients into two categories:

* **0 – No Diabetes**
* **1 – Diabetes**

The dataset contains information such as glucose level, blood pressure, BMI, insulin, age, number of pregnancies, and diabetes pedigree information.

This project demonstrates the complete basic machine learning workflow, including data loading, data cleaning, preprocessing, model training, prediction, evaluation, and visualization.

## Objectives

* Analyze a diabetes dataset.
* Identify and handle missing values.
* Prepare data for machine learning.
* Split the dataset into training and testing data.
* Standardize numerical features.
* Train a Logistic Regression classification model.
* Predict diabetes outcomes.
* Evaluate model performance.
* Visualize the relationship between glucose level and BMI.

## Technologies Used

* **Python**
* **Pandas** – Data loading and data manipulation
* **Matplotlib** – Data visualization
* **Scikit-learn** – Machine learning and model evaluation

## Dataset

The dataset contains **442 records and 9 columns**.

### Features

| Feature           | Description                      |
| ----------------- | -------------------------------- |
| pregnancies       | Number of pregnancies            |
| glucose           | Glucose level                    |
| blood_pressure    | Blood pressure measurement       |
| skin_thickness    | Skin thickness measurement       |
| insulin           | Insulin level                    |
| bmi               | Body Mass Index                  |
| diabetes_pedigree | Diabetes pedigree function value |
| age               | Age of the person                |
| outcome           | Diabetes prediction target       |

### Target Variable

* `0` → No Diabetes
* `1` → Diabetes

## Machine Learning Workflow

The project follows these steps:

```text
Dataset
   ↓
Data Loading
   ↓
Data Inspection
   ↓
Missing Value Handling
   ↓
Feature & Target Separation
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Logistic Regression
   ↓
Prediction
   ↓
Model Evaluation
   ↓
Visualization
```

## Data Preprocessing

The project performs the following preprocessing steps:

1. Loads the dataset using Pandas.
2. Checks the dataset structure and missing values.
3. Replaces missing numerical values with their respective median values.
4. Separates the input features from the target variable.
5. Splits the data into:

   * 80% training data
   * 20% testing data
6. Uses `StandardScaler` to standardize the input features.

## Machine Learning Model

### Logistic Regression

Logistic Regression is used because this is a **binary classification problem**.

The model predicts whether the input belongs to:

```text
0 → No Diabetes
1 → Diabetes
```

The model is trained using the standardized training data and then used to predict outcomes for the test data.

## Model Evaluation

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* Classification Report

Using the included dataset and the current code workflow, the model achieves approximately:

**Test Accuracy: 76.40%**

The exact result can vary if the dataset, preprocessing, or train-test split is changed.

## Visualization

The project generates a scatter plot showing the relationship between:

* **Glucose Level**
* **BMI**

The points are grouped according to the diabetes outcome.

## Example Prediction

The project also demonstrates prediction for a new person's health measurements, such as:

* Pregnancies: 2
* Glucose: 130
* Blood Pressure: 80
* Skin Thickness: 25
* Insulin: 100
* BMI: 28.5
* Diabetes Pedigree: 0.45
* Age: 35

The trained model predicts whether the example person belongs to the diabetes or no-diabetes class.

## Project Files

```text
Diabetes_Prediction/
│
├── diabetes.csv
├── diabetes_prediction.py
├── requirements.txt
└── README.md
```

### `diabetes.csv`

Contains the dataset used for training and testing the machine learning model.

### `diabetes_prediction.py`

Contains the complete Python implementation for:

* Data loading
* Data cleaning
* Preprocessing
* Model training
* Prediction
* Evaluation
* Visualization

### `requirements.txt`

Contains the Python libraries required to run the project.

## Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the Project Folder

```bash
cd Diabetes_Prediction
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Project

```bash
python diabetes_prediction.py
```

## Requirements

The project requires:

```text
pandas
matplotlib
scikit-learn
```

You can install all dependencies using:

```bash
pip install -r requirements.txt
```

## Applications

This project demonstrates how machine learning can be applied to healthcare-related datasets for predictive analysis and classification.

It can be useful as a **learning project for students studying Python, Data Science, Machine Learning, and Data Analytics**.

## Future Improvements

The project can be further improved by:

* Comparing multiple machine learning algorithms.
* Adding a user-friendly web interface.
* Adding interactive visualizations.
* Performing feature selection.
* Using cross-validation.
* Hyperparameter tuning.
* Adding ROC-AUC evaluation.
* Deploying the model as a web application.

## Disclaimer

This project is intended for **educational and demonstration purposes only**. The prediction produced by this machine learning model should not be considered a medical diagnosis or used for clinical decision-making.
