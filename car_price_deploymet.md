# Car Price Prediction App Documentation

## File

- `car_price_deploymet.py`

## Purpose

This Streamlit app loads the trained machine learning model and predicts the price of a car from user inputs.

## Features

- User selects fuel type
- User sets horsepower using a slider
- User selects transmission type
- User selects number of seats
- Clicking the prediction button calculates the estimated price
- Displays the result in a success message

## Model Loading

The app loads the trained model from:

- `car_price_model.joblib`

## Input Fields

- Fuel Type: `Petrol`, `Diesel`, `Electric`, `Hybrid`
- Horsepower: slider from 50 to 1000
- Transmission: `Automatic` or `Manual`
- Seats: `2`, `4`, `5`, `7`

## Prediction Flow

1. User enters car specifications.
2. The app creates a pandas DataFrame matching the model input format.
3. The model predicts the car price.
4. The result is displayed with formatting such as `$24,000.00`.

## Libraries Used

- `streamlit`
- `pandas`
- `joblib`

## Notes

The file name contains `deploymet` instead of `deployment`, but the app works as a deployment interface for the trained ML model.
