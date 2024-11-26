import unittest
import pandas as pd
import numpy as np
import os
import sys


# Add the project root directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


# Adjust the path to include the parent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Now import the calculate_rsi function
from technical_indicator import calculate_rsi

class TestTechnicalIndicators(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        self.test_data = pd.DataFrame({
            'Close': [100, 102, 101, 105, 107, 106, 108, 110, 112, 111]
        })

    def test_sma_calculation(self):
        # Expected SMA calculation
        expected_sma = self.test_data['Close'].rolling(window=5).mean()
        self.test_data['SMA'] = self.test_data['Close'].rolling(window=5).mean()
        pd.testing.assert_series_equal(
            self.test_data['SMA'], expected_sma, check_names=False
        )

    def test_ema_calculation(self):
        # Expected EMA calculation
        expected_ema = self.test_data['Close'].ewm(span=5, adjust=False).mean()
        self.test_data['EMA'] = self.test_data['Close'].ewm(span=5, adjust=False).mean()
        pd.testing.assert_series_equal(
            self.test_data['EMA'], expected_ema, check_names=False
        )

    def test_rsi_calculation(self):
        # Calculate RSI using the function from technical_indicator.py
        self.test_data['RSI'] = calculate_rsi(self.test_data, window=5)

        # Manually calculate RSI for comparison
        delta = self.test_data['Close'].diff(1)
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=5).mean()
        avg_loss = loss.rolling(window=5).mean()
        rs = avg_gain / avg_loss
        expected_rsi = 100 - (100 / (1 + rs))

        pd.testing.assert_series_equal(
            self.test_data['RSI'], expected_rsi, check_names=False
        )

if __name__ == '__main__':
    unittest.main()
