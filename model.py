# rtl-cld-predictor/src/model.py
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LinearRegression

def create_random_forest_model(n_estimators=100, random_state=42):
    """Creates a Random Forest Regression model."""
    return RandomForestRegressor(n_estimators=n_estimators, random_state=random_state)

def create_mlp_model(hidden_layer_sizes=(100, 50), random_state=42):
    """Creates an MLP Regression model."""
    return MLPRegressor(hidden_layer_sizes=hidden_layer_sizes, random_state=random_state, max_iter=500)

def create_linear_regression_model():
    """Creates a Linear Regression model."""
    return LinearRegression()
