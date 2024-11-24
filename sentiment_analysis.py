import pandas as pd
from transformers import pipeline

# Load the CSV file containing the top articles
news_df = pd.read_csv("top_articles_by_day.csv")

# Load the sentiment-analysis pipeline from Hugging Face
sentiment_pipeline = pipeline("sentiment-analysis")

# Function for Hugging Face sentiment analysis
def get_sentiment_huggingface(text):
    if pd.isna(text):  # Handle missing values
        return None
    result = sentiment_pipeline(text)
    return result[0]['label']  # Returns 'POSITIVE' or 'NEGATIVE'

# Apply sentiment analysis to 'title' and 'description'
news_df['title_sentiment_hf'] = news_df['title'].apply(get_sentiment_huggingface)
news_df['description_sentiment_hf'] = news_df['description'].apply(get_sentiment_huggingface)

# Save the updated DataFrame to a new CSV file
news_df.to_csv("top_articles_with_hf_sentiment.csv", index=False)

# Print confirmation
print("Sentiment analysis added and saved to 'top_articles_with_hf_sentiment.csv'")
