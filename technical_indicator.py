import pandas as pd

# Load the merged data
merged_data = pd.read_csv("merged_stock_and_news_data.csv")

# Remove the first row of the company tag
merged_data = merged_data.drop(merged_data.index[0]).reset_index(drop=True)

# Ensure the 'Close' column is numeric
merged_data['Close'] = pd.to_numeric(merged_data['Close'], errors='coerce')

# Recalculate the SMA, EMA, and RSI
merged_data['SMA'] = merged_data['Close'].rolling(window=5).mean()
merged_data['EMA'] = merged_data['Close'].ewm(span=5, adjust=False).mean()

# Define RSI calculation function
def calculate_rsi(data, window=5):
    delta = data['Close'].diff(1)  # Difference in price
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()  # Average gain
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()  # Average loss
    rs = gain / loss  # Relative Strength
    rsi = 100 - (100 / (1 + rs))  # RSI formula
    return rsi

# Calculate and add RSI column
merged_data['RSI'] = calculate_rsi(merged_data)

# Display the updated DataFrame
print(merged_data.head())

# Optionally, save the updated DataFrame to a new CSV
merged_data.to_csv("final_data.csv", index=False)
