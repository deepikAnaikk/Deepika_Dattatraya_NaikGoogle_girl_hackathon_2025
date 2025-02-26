# rtl-cld-predictor/src/trainer.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import time
from src.data_loader import load_data, preprocess_data
from src.model import create_random_forest_model, create_mlp_model, create_linear_regression_model

def train_and_evaluate(model, features, labels, test_size=0.2, random_state=42):
    """Trains and evaluates a model."""
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=test_size, random_state=random_state)
    start_time = time.time()
    model.fit(X_train, y_train)
    training_time = time.time() - start_time
    start_time = time.time()
    y_pred = model.predict(X_test)
    prediction_time = time.time() - start_time
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Training Time: {training_time:.4f} seconds")
    print(f"Prediction Time: {prediction_time:.4f} seconds")
    print(f"MSE: {mse:.4f}, MAE: {mae:.4f}, R-squared: {r2:.4f}")
    return mse, mae, r2

if __name__ == "__main__":
    data = load_data()
    if data is not None:
        features = ["fan_in", "fan_out", "lines_of_code"] #adjust features
        labels = "cld"
        features_data, labels_data = preprocess_data(data, features, labels)
        if features_data is not None and labels_data is not None:
            print("Random Forest:")
            train_and_evaluate(create_random_forest_model(), features_data, labels_data)
            print("\
