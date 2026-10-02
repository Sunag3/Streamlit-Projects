import streamlit as st
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
import joblib



data = pd.DataFrame({
    "fuel_type": ["Petrol", "Diesel", "Electric", "Hybrid"],
    "horsepower": [150, 200, 300, 250],
    "transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "seats": [5, 5, 4, 5],
    "price": [20000, 25000, 35000, 30000]
})


# ML Pipeline

x = data[["fuel_type", "horsepower", "transmission", "seats"]]

y = data["price"]

categorical_features = ["fuel_type", "transmission"]

# Apply one-hot encoding to categorical features

preprocessor = ColumnTransformer(
    transformers=[
        ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ],)


# Create a Model

model = Pipeline(steps=[("preprocessor", preprocessor), ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))])


# Store this model in a model registry for future use
# in local store in job lib or pickle file


model.fit(x, y)
joblib.dump(model, "car_price_model.joblib")