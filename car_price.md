# Car Price Training App Documentation

## File

- `car_price.py`

## Purpose

This script trains a machine learning model to predict car price based on a few key attributes such as fuel type, horsepower, transmission, and number of seats.

## Features

- Builds a sample car dataset
- Uses `OneHotEncoder` for categorical data
- Creates a machine learning pipeline with a `RandomForestRegressor`
- Trains the model on the sample dataset
- Saves the trained model to `car_price_model.joblib`

## Machine Learning Pipeline

The model uses:

- `ColumnTransformer` for preprocessing
- `OneHotEncoder` for categorical variables like fuel type and transmission
- `RandomForestRegressor` as the prediction model

## Key Variables

- `fuel_type`
- `horsepower`
- `transmission`
- `seats`
- `price`

## Output

The trained model is stored in:

- `car_price_model.joblib`

## Libraries Used

- `pandas`
- `scikit-learn`
- `joblib`

## Notes

This file is responsible for model creation and training, not for user interaction. The actual app interface is handled by the deployment file.
