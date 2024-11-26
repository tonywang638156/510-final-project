import unittest
import os
import pandas as pd
from yahooAPI_stock_data import collect_stock_data
import sys

# Add the project root directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


class TestStockDataCollection(unittest.TestCase):
    def setUp(self):
        # Remove the CSV file if it exists before each test
        self.file_path = "stock_data.csv"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_collect_stock_data_creates_file(self):
        # Run the data collection function
        collect_stock_data()
        # Check if the CSV file has been created
        self.assertTrue(os.path.exists(self.file_path), "CSV file was not created.")

    def test_collect_stock_data_content(self):
        # Run the data collection function
        collect_stock_data()
        # Load the data
        stock_data = pd.read_csv(self.file_path)
        # Check if the DataFrame is not empty
        self.assertFalse(stock_data.empty, "CSV file is empty.")
        # Check for expected columns
        expected_columns = ["date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
        self.assertTrue(all(column in stock_data.columns for column in expected_columns),
                        "CSV file does not contain all expected columns.")

    def tearDown(self):
        # Clean up: remove the CSV file after each test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

if __name__ == "__main__":
    unittest.main()
