import yfinance as yf
from datetime import datetime, timedelta
import os

def collect_stock_data():
    # Define the stock symbol and date range
    stock_symbol = "AAPL" 
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)  # 30 days ago

    # Download stock data from Yahoo Finance
    stock_data = yf.download(stock_symbol, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))

    # Reset index and save the date column
    stock_data.reset_index(inplace=True)
    stock_data.rename(columns={"Date": "date"}, inplace=True)

    # Define the file path
    file_path = "stock_data.csv"

    # Save stock data to CSV
    stock_data.to_csv(file_path, index=False)
    
    print("Stock data collected and saved to 'stock_data.csv'")

if __name__ == "__main__":
    # Check if the script is being run directly
    if not os.path.exists("stock_data.csv"):
        collect_stock_data()
    else:
        print("Stock data already exists.")
