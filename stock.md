# Stock Price Analyzer Documentation

## File

- `stock.py`

## Purpose

This app analyzes stock prices using the Yahoo Finance API and visualizes the trend of a stock over time.

## Features

- User enters a stock ticker symbol such as `NVDA`
- User selects start and end dates
- Data is fetched using `yfinance`
- Displays stock data in a table
- Shows line chart of closing price
- Shows bar chart of trading volume
- Shows percentage change of closing price

## Libraries Used

- `streamlit`
- `yfinance`
- `datetime`

## Main Workflow

1. The user enters a stock ticker.
2. The app selects a date range.
3. `yf.download()` fetches stock market history.
4. The app displays the raw data, close price trend, and volume trend.
5. The final chart visualizes percentage change in the closing price.

## Important Note

The app should validate whether the returned data is empty before plotting. For invalid tickers or date ranges with no market activity, `ticker_data['Close']` and `ticker_data['Volume']` may raise errors.

## Suggested Improvements

- Add validation for empty or missing stock data
- Show error messages with `st.error()` when a ticker is invalid
- Add stock summary metrics such as min, max, and average price
- Add technical indicators like moving averages
- Allow multiple stock comparison
