import yfinance as yf
import pandas as pd
import ta

# Function to fetch historical stock data and add technical analysis features
def get_stock_data_with_features(ticker, start_date, end_date):
    # Fetch historical data
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    # Add individual technical analysis features using the ta library
    stock_data["SMA_50"] = ta.sma_indicator(stock_data["Close"], window=50)
    stock_data["SMA_200"] = ta.sma_indicator(stock_data["Close"], window=200)
    stock_data["RSI"] = ta.rsi(stock_data["Close"], window=14)
    stock_data["MACD"] = ta.macd_diff(stock_data["Close"], window_slow=26, window_fast=12, window_sign=9)

    return stock_data

# Define the stock symbol, start date, and end date
ticker_symbol = "MSFT"
start_date = "2022-01-01"
end_date = "2023-01-01"

# Get stock data with features
stock_data_with_features = get_stock_data_with_features(ticker_symbol, start_date, end_date)

# Display the resulting DataFrame
print(stock_data_with_features.head())
