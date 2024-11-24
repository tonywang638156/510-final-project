import pandas as pd

# Load stock data (e.g., from a CSV file)
stock_data = pd.read_csv("stock_data.csv")
stock_data['date'] = pd.to_datetime(stock_data['date']).dt.tz_localize(None)  # Remove timezone if exists

# Load the news data (e.g., from a CSV file)
news_data = pd.read_csv("top_articles_with_hf_sentiment.csv")
news_data['publishedAt'] = pd.to_datetime(news_data['publishedAt'])
news_data['date'] = news_data['publishedAt'].dt.date  # Extract only the date part

# Ensure both 'Date' columns are of the same format (datetime64[ns], without timezone)
stock_data['date'] = stock_data['date'].dt.date  # Convert to date format only if needed

# Merge the two datasets on the 'Date' column (using left join to preserve all stock data)
merged_data = pd.merge(stock_data, news_data, on='date', how='left')

# Save the merged data to a new CSV
merged_data.to_csv("merged_stock_and_news_data.csv", index=False)
