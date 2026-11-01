# 🏡 House Price Prediction Using MLOps



## 📌 1. Project Overview

This project focuses on predicting house prices using Machine Learning and MLOps concepts.

A Linear Regression algorithm is used to predict house prices based on property features such as area, number of bedrooms, number of bathrooms, and house age.

The project demonstrates a complete Machine Learning workflow, from dataset generation and model training to experiment tracking and API deployment.

## 🎯 2. Project Objectives

- Predict house prices using Machine Learning.
- Generate and prepare a structured dataset.
- Train a Linear Regression model.
- Evaluate model performance.
- Track experiments using MLflow.
- Save the trained model using Joblib.
- Deploy the model using FastAPI.

## 🛠️ 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| NumPy | Numerical Operations |
| Pandas | Data Processing |
| Scikit-learn | Machine Learning |
| Linear Regression | Prediction Algorithm |
| MLflow | Experiment Tracking |
| Joblib | Model Saving |
| FastAPI | API Development |
| Uvicorn | API Server |
| Git & GitHub | Version Control |

## 🧠 4. Machine Learning Algorithm

**Linear Regression**

Linear Regression is used to estimate house prices based on the relationship between property features and their prices.

**Input Features:**
- Area (Square Feet)
- Number of Bedrooms
- Number of Bathrooms
- House Age

**Output:**
- Predicted House Price

## 📂 5. Project Structure

```text
amit-house-price-mlops/
│
├── data/
│   └── house_prices.csv
│
├── models/
│   └── house_model.joblib
│
├── generate_data.py
├── train.py
├── api.py
├── requirements.txt
└── .gitignore
```

## ⚙️ 6. Project Workflow

1. Dataset Generation
2. Data Preparation
3. Model Training
4. Model Evaluation
5. MLflow Experiment Tracking
6. Model Saving
7. FastAPI Deployment
8. House Price Prediction

## 🚀 7. Installation and Execution

### Step 1: Clone the Repository

```bash
git clone <repository-url>
```

### Step 2: Open Project Folder

```bash
cd amit-house-price-mlops
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Generate Dataset

```bash
python generate_data.py
```

### Step 5: Train the Model

```bash
python train.py
```

The trained model is saved inside the `models` folder.

### Step 6: Run FastAPI Application

```bash
uvicorn api:app --reload
```

### Step 7: Open API Documentation

Open the following address in your browser:

`http://127.0.0.1:8000/docs`

Use the `/predict` endpoint to test house price predictions.

## 📊 8. Model Evaluation

The model is evaluated using the following metrics:

- **MAE:** Mean Absolute Error
- **RMSE:** Root Mean Squared Error
- **R² Score:** Coefficient of Determination

These metrics help measure the prediction performance of the model.

## 📈 9. MLflow Experiment Tracking

MLflow is used to track model training experiments, parameters, and evaluation metrics.



## 🖥️ 10. Project Output

### A. Sample Input

The following house details were submitted to the prediction API:

| Feature | Input Value |
|---|---:|
| Area | 1500 sq. ft. |
| Bedrooms | 3 |
| Bathrooms | 2 |
| House Age | 5 years |

### B. Prediction Result

**Predicted House Price: ₹48,14,500.10**

The trained Linear Regression model successfully generated a predicted house price for the given input.

### C. FastAPI Response

| Parameter | Result |
|---|---|
| API Endpoint | POST /predict |
| API Status | 200 OK |
| Prediction Status | Successful |
| Model | Linear Regression |

### D. Model Training Output

The training process successfully:
- Trained the Linear Regression model.
- Calculated MAE, RMSE, and R² Score.
- Recorded experiment details in MLflow.
- Saved the trained model as `house_model.joblib`.

### E. Final Output

The project successfully performs house price prediction through a FastAPI application using a trained Machine Learning model.

## 📁 11. Dataset Information

The project uses a synthetically generated dataset containing 200 house records.

Dataset features include:
- Area
- Bedrooms
- Bathrooms
- House Age
- House Price

**Note:** This dataset is synthetic and intended for educational and demonstration purposes. The predicted price should not be considered an actual real-estate market valuation.

## 🌟 12. Key Features

- Machine Learning-based house price prediction.
- Automated dataset generation.
- Model training and evaluation.
- MLflow experiment tracking.
- Model serialization using Joblib.
- REST API development using FastAPI.
- Git and GitHub version control.

## 🔮 13. Future Improvements

- Use real-world housing datasets.
- Compare different Machine Learning algorithms.
- Improve model accuracy and generalization.
- Add automated model retraining.
- Deploy the application on a cloud platform.
- Implement CI/CD pipelines.

## 👨‍💻 14. Author

**Amit**

Machine Learning and MLOps Project

## 🏁 15. Conclusion

This project demonstrates an end-to-end Machine Learning workflow by combining Linear Regression, MLflow, Joblib, and FastAPI.

It provides practical experience in developing, training, evaluating, tracking, and deploying a Machine Learning model.

The project serves as a foundation for learning real-world Machine Learning and MLOps concepts.

