import streamlit as st
import pandas as pd
import streamlit as st
import joblib

st.title("Car Price Prediction App")

st.write("Enter the details of the car to predict its price.")

model = joblib.load("car_price_model.joblib")

# define structure of the input data

col1,col2,col3 = st.columns(3)

with col1:
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric", "Hybrid"])
    horsepower = st.slider("Horsepower", min_value=50, max_value=1000, value=150)
    

with col2:
    transmission = st.selectbox("Transmission", ["Automatic", "Manual"])
    seats = st.selectbox("Number of Seats", [2, 4, 5, 7])


# Button to predict the price

if st.button("Predict Price"):
    input_data = pd.DataFrame({
        "fuel_type": [fuel_type],
        "horsepower": [horsepower],
        "transmission": [transmission],
        "seats": [seats]
    })

    predicted_price = model.predict(input_data)[0]

    st.success(f"The predicted price of the car is: ${predicted_price:,.2f}")
