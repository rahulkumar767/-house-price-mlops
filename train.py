
import pandas as pd
import mlflow
import mlflow.sklearn
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("data/house_prices.csv")

# Select X and y
X = df[["area_sqft", "bedrooms", "bathrooms", "house_age"]]
y = df["price"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Set MLflow experiment
mlflow.set_experiment("House Price Prediction")

# Start MLflow run
with mlflow.start_run():

    # Train model
    model.fit(X_train, y_train)
    # Create models folder
os.makedirs("models", exist_ok=True)

# Save trained model
joblib.dump(model, "models/house_model.joblib")

print("Model saved successfully!")

    # Predict
y_pred = model.predict(X_test)

    # Calculate metrics
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2 = r2_score(y_test, y_pred)

    # Log parameters
mlflow.log_param("model", "Linear Regression")
mlflow.log_param("test_size", 0.2)
mlflow.log_param("random_state", 42)

    # Log metrics
mlflow.log_metric("MAE", mae)
mlflow.log_metric("RMSE", rmse)
mlflow.log_metric("R2_Score", r2)

    # Log model
mlflow.sklearn.log_model(
        model,
        artifact_path="house_price_model"
    )

print("Model trained successfully!")
print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)

print("\nMLflow Tracking Completed!")
