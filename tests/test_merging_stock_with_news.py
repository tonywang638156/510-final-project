# test_merging_stock_with_news.py

import unittest
import pandas as pd
import os

class TestMergingStockWithNews(unittest.TestCase):
    def setUp(self):
        # Create sample stock data
        self.stock_data = pd.DataFrame({
            'date': pd.date_range(start='2021-01-01', periods=5, freq='D'),
            'Close': [150, 152, 151, 153, 155],
            'Open': [148, 150, 149, 151, 153],
            'High': [151, 153, 152, 154, 156],
            'Low': [147, 149, 148, 150, 152]
        })
        self.stock_data.to_csv('stock_data.csv', index=False)

        # Create sample news data
        self.news_data = pd.DataFrame({
            'publishedAt': pd.date_range(start='2021-01-01', periods=3, freq='2D'),
            'headline': ['News A', 'News B', 'News C'],
            'description': ['Desc A', 'Desc B', 'Desc C'],
            'sentiment': ['Positive', 'Negative', 'Neutral']
        })
        self.news_data.to_csv('top_articles_with_hf_sentiment.csv', index=False)
    
    def test_merge_stock_and_news_data(self):
        # Load stock data
        stock_data = pd.read_csv("stock_data.csv")
        stock_data['date'] = pd.to_datetime(stock_data['date']).dt.tz_localize(None)

        # Load news data
        news_data = pd.read_csv("top_articles_with_hf_sentiment.csv")
        news_data['publishedAt'] = pd.to_datetime(news_data['publishedAt'])
        news_data['date'] = news_data['publishedAt'].dt.date  # Extract only the date part

        # Ensure both 'date' columns are of the same format
        stock_data['date'] = stock_data['date'].dt.date

        # Merge the two datasets on the 'date' column
        merged_data = pd.merge(stock_data, news_data, on='date', how='left')

        # Expected merged data
        expected_data = pd.DataFrame({
            'date': pd.to_datetime([
                '2021-01-01', '2021-01-02', '2021-01-03',
                '2021-01-04', '2021-01-05'
            ]).date,
            'Close': [150, 152, 151, 153, 155],
            'Open': [148, 150, 149, 151, 153],
            'High': [151, 153, 152, 154, 156],
            'Low': [147, 149, 148, 150, 152],
            'publishedAt': [
                pd.to_datetime('2021-01-01'),
                pd.NaT,
                pd.to_datetime('2021-01-03'),
                pd.NaT,
                pd.to_datetime('2021-01-05')
            ],
            'headline': ['News A', None, 'News B', None, 'News C'],
            'description': ['Desc A', None, 'Desc B', None, 'Desc C'],
            'sentiment': ['Positive', None, 'Negative', None, 'Neutral']
        })

        # Assert that the merged data matches the expected data
        pd.testing.assert_frame_equal(merged_data.reset_index(drop=True), expected_data.reset_index(drop=True))

    def tearDown(self):
        # Clean up the CSV files created during the test
        if os.path.exists('stock_data.csv'):
            os.remove('stock_data.csv')
        if os.path.exists('top_articles_with_hf_sentiment.csv'):
            os.remove('top_articles_with_hf_sentiment.csv')
        if os.path.exists('merged_stock_and_news_data.csv'):
            os.remove('merged_stock_and_news_data.csv')

if __name__ == '__main__':
    unittest.main()
