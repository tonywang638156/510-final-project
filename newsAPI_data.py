import requests
import pandas as pd
from datetime import datetime, timedelta

# Define your NewsAPI key
news_api_key = "56a09efdc146428fbf0385e61c134591"

# Base URL for NewsAPI
news_base_url = "https://newsapi.org/v2/everything"

# Define the date range (last 30 days)
end_date = datetime.now()
start_date = end_date - timedelta(days=30)

# Prepare a list to store the most relevant articles for each date
top_articles = []

# Loop through each day in the past 30 days
for i in range(30):
    # Calculate the date range for the current day
    date = start_date + timedelta(days=i)
    next_date = date + timedelta(days=1)
    
    # Define the parameters for the API request
    news_params = {
        'q': 'apple stock',       # Search query
        'language': 'en',          # Language of the articles
        'sortBy': 'popularity',    # Sort articles by popularity
        'from': date.strftime('%Y-%m-%d'),
        'to': next_date.strftime('%Y-%m-%d'),
        'apiKey': news_api_key,
        'pageSize': 3  # Fetch up to 10 articles per day to find the best one
    }
    
    # Make the API request
    response = requests.get(news_base_url, params=news_params)
    
    if response.status_code == 200:
        # Parse the JSON response
        news_data = response.json()
        articles = news_data.get('articles', [])
        
        # Select the most relevant article (the first one, since it's sorted by popularity)
        if articles:
            most_relevant_article = articles[0]  # The first article is the most popular
            top_articles.append({
                "date": date.strftime('%Y-%m-%d'),
                "title": most_relevant_article.get("title"),
                "description": most_relevant_article.get("description"),
                "url": most_relevant_article.get("url"),
                "source": most_relevant_article.get("source", {}).get("name"),
                "publishedAt": most_relevant_article.get("publishedAt"),
            })
    else:
        print(f"Failed to fetch news for {date.strftime('%Y-%m-%d')}: {response.status_code}")
        print(response.text)

# Convert the results to a DataFrame
top_articles_df = pd.DataFrame(top_articles)

# Save the DataFrame to a CSV file
if not top_articles_df.empty:
    top_articles_df.to_csv("top_articles_by_day.csv", index=False)
    print("Top articles saved to 'top_articles_by_day.csv'")
else:
    print("No articles found for the given date range.")
