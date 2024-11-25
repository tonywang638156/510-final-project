import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'final_data.csv'  # Replace with your file path if needed
data = pd.read_csv(file_path)

# Convert date column to datetime
data['date'] = pd.to_datetime(data['date'])

# Filter necessary columns for analysis
analysis_data = data[['date', 'Adj Close', 'Volume', 'SMA', 'EMA', 'RSI', 'title_sentiment_hf', 'description_sentiment_hf']]

# Drop rows with NaN sentiment values for better analysis
analysis_data.dropna(subset=['title_sentiment_hf', 'description_sentiment_hf'], inplace=True)

# Map sentiment categories to numerical values
sentiment_mapping = {'POSITIVE': 1, 'NEGATIVE': -1, 'NEUTRAL': 0}
analysis_data['title_sentiment_hf'] = analysis_data['title_sentiment_hf'].map(sentiment_mapping)
analysis_data['description_sentiment_hf'] = analysis_data['description_sentiment_hf'].map(sentiment_mapping)

# Calculate correlations
correlation_matrix = analysis_data.corr()

# Visualization: Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.png')  # Save as PNG
plt.close()

# Visualization: Distribution of sentiment scores
plt.figure(figsize=(10, 5))
sns.histplot(analysis_data['title_sentiment_hf'], bins=3, kde=False, label='Title Sentiment', color='red')
sns.histplot(analysis_data['description_sentiment_hf'], bins=3, kde=False, label='Description Sentiment', color='green')
plt.title('Distribution of Sentiment Scores')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('sentiment_score_distribution.png')  # Save as PNG
plt.close()

# Visualization: Boxplot of stock prices vs sentiment
plt.figure(figsize=(10, 6))
sns.boxplot(x='title_sentiment_hf', y='Adj Close', data=analysis_data)
plt.title('Stock Prices by Title Sentiment')
plt.xlabel('Title Sentiment')
plt.ylabel('Adjusted Close Price')
plt.savefig('stock_prices_by_title_sentiment.png')  # Save as PNG
plt.close()

plt.figure(figsize=(10, 6))
sns.boxplot(x='description_sentiment_hf', y='Adj Close', data=analysis_data)
plt.title('Stock Prices by Description Sentiment')
plt.xlabel('Description Sentiment')
plt.ylabel('Adjusted Close Price')
plt.savefig('stock_prices_by_description_sentiment.png')  # Save as PNG
plt.close()
