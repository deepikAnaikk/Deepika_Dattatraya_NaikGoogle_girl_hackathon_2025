import joblib
import numpy as np
import pandas as pd  # ✅ Add this missing import

# Load the trained model
model = joblib.load("depth_predictor_model.pkl")

# ✅ Define feature names correctly
feature_names = ["gate_count", "timing"]

# ✅ Fix test input (use a DataFrame with correct feature names)
test_input = pd.DataFrame([[150, 0.35]], columns=feature_names)
predicted_depth = model.predict(test_input)

print(f"Predicted Logic Depth: {predicted_depth[0]:.2f}")

