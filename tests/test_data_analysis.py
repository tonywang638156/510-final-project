import unittest
import pandas as pd
from data_analysis import analysis_data  # Update this import path as per your project structure
import sys
import os

# Add the project root directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


class TestDataAnalysis(unittest.TestCase):
    def setUp(self):
        """Set up test data for analysis."""
        self.test_data = pd.DataFrame({
            'date': ['2024-10-01', '2024-10-02', '2024-10-03'],
            'Adj Close': [230.15, 231.12, 233.45],
            'title_sentiment_hf': ['POSITIVE', 'NEGATIVE', 'NEUTRAL'],
            'description_sentiment_hf': ['NEUTRAL', 'POSITIVE', 'NEGATIVE']
        })
        self.test_data['date'] = pd.to_datetime(self.test_data['date'])

    def test_data_loading(self):
        """Test if the dataset loads correctly."""
        self.assertEqual(len(self.test_data), 3, "Dataset length mismatch")

    def test_sentiment_mapping(self):
        """Test mapping of sentiment to numerical values."""
        sentiment_mapping = {'POSITIVE': 1, 'NEGATIVE': -1, 'NEUTRAL': 0}
        self.test_data['title_sentiment_hf'] = self.test_data['title_sentiment_hf'].map(sentiment_mapping)
        self.test_data['description_sentiment_hf'] = self.test_data['description_sentiment_hf'].map(sentiment_mapping)
        
        self.assertTrue(all(self.test_data['title_sentiment_hf'].isin([-1, 0, 1])), "Title sentiment mapping failed")
        self.assertTrue(all(self.test_data['description_sentiment_hf'].isin([-1, 0, 1])), "Description sentiment mapping failed")

    def test_correlation_computation(self):
        """Test if the correlation matrix computes successfully."""
        # Apply sentiment mapping
        sentiment_mapping = {'POSITIVE': 1, 'NEGATIVE': -1, 'NEUTRAL': 0}
        self.test_data['title_sentiment_hf'] = self.test_data['title_sentiment_hf'].map(sentiment_mapping)
        self.test_data['description_sentiment_hf'] = self.test_data['description_sentiment_hf'].map(sentiment_mapping)
        
        # Compute correlation matrix
        correlation_matrix = self.test_data.corr()
        self.assertFalse(correlation_matrix.empty, "Correlation matrix computation failed")
        self.assertIn('Adj Close', correlation_matrix.columns, "Correlation matrix missing expected columns")

    def test_missing_values_handling(self):
        """Test if missing values are handled correctly."""
        # Add missing values
        self.test_data.loc[0, 'Adj Close'] = None
        self.assertTrue(self.test_data.isnull().any().any(), "Missing values not present as expected")
        
        # Drop missing values
        clean_data = self.test_data.dropna()
        self.assertFalse(clean_data.isnull().any().any(), "Missing values not removed successfully")
        self.assertEqual(len(clean_data), 2, "Incorrect number of rows after dropping missing values")

if __name__ == '__main__':
    unittest.main()
