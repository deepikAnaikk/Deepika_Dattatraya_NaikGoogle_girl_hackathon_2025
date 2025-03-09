import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
data = pd.read_csv(r"C:\Users\deepi\Desktop\new me\RTL_Project\data.csv")

# Display first few rows
print("Dataset Preview:")
print(data.head())

# Extract features and target
X = data[['gate_count', 'timing']]  # Features
y = data['logic_depth']  # Target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Machine Learning model (Random Forest)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make prediction
y_pred = model.predict(X_test)

# Evaluate performance
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae:.3f}")

# Plot feature importance
plt.figure(figsize=(8, 4))
sns.barplot(x=model.feature_importances_, y=X.columns)
plt.title("Feature Importance")
plt.show()

import joblib  # Library for saving models

# Save the trained model
joblib.dump(model, "depth_predictor_model.pkl")
print("Model saved as depth_predictor_model.pkl")
