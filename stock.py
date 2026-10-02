import streamlit as st
import yfinance as yf
import datetime as dt

st.title(" Stock Price Analyser")
st.subheader("This app allows you to analyze stock prices and visualize trends over time.")

col1,col2 = st.columns(2)
# ticker = yf.Ticker("NVDA")

ticker = st.text_input("Enter Stock Ticker Symbol", "NVDA")



with col1:
    start_date = st.date_input("Enter Start Date (YYYY-MM-DD)", dt.datetime(2026, 1, 1))
with col2:
    end_date = st.date_input("Enter End Date (YYYY-MM-DD)", dt.datetime.now())

ticker_data = yf.download(ticker, start=start_date, end=end_date)
# ticker_data = yf.Ticker(ticker).history(period="1mo")

st.write("### Stock Price Data for " + ticker)
st.dataframe(ticker_data)

st.write("### Closing Price Trend")
st.line_chart(ticker_data['Close'])

st.write("### Volume Trend")
st.bar_chart(ticker_data['Volume'])


st.subheader("Price Movement Analysis")


st.line_chart(ticker_data['Close'].pct_change().dropna(), use_container_width=True)