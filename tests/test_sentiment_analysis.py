import unittest
from unittest.mock import patch
from sentiment_analysis import get_sentiment_huggingface

class TestSentimentAnalysis(unittest.TestCase):
    def test_positive_sentiment(self):
        """Test if positive sentiment is detected correctly."""
        text = "The stock market is performing exceptionally well today!"
        result = get_sentiment_huggingface(text)
        self.assertEqual(result, "POSITIVE", "Failed to identify positive sentiment")

    def test_negative_sentiment(self):
        """Test if negative sentiment is detected correctly."""
        text = "The company's profits dropped significantly this quarter."
        result = get_sentiment_huggingface(text)
        self.assertEqual(result, "NEGATIVE", "Failed to identify negative sentiment")

    def test_neutral_sentiment(self):
        """Test if neutral sentiment is handled correctly."""
        text = None  # Neutral case with no text provided
        result = get_sentiment_huggingface(text)
        self.assertIsNone(result, "Failed to handle missing text correctly")

    @patch('scripts.sentiment_analysis.pipeline')
    def test_mock_pipeline(self, mock_pipeline):
        """Test if the Hugging Face pipeline is called correctly."""
        # Mock the pipeline's return value
        mock_pipeline.return_value = lambda text: [{"label": "POSITIVE", "score": 0.98}]
        
        text = "The market is rising steadily."
        
        with patch('scripts.sentiment_analysis.sentiment_pipeline', mock_pipeline.return_value):
            result = get_sentiment_huggingface(text)
            self.assertEqual(result, "POSITIVE", "Mocked pipeline returned incorrect sentiment")

if __name__ == '__main__':
    unittest.main()
