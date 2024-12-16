import os
import pandas as pd
import yfinance as yf
from datetime import datetime
from dateutil.relativedelta import relativedelta
from config import DATA_FILE_PATH, REPORT_PATH  # Import constants from config
from Utilities.data_loader import load_test_data
import pytest

class DataManager:
    def __init__(self):
        self.data = None
        self.stockname = None
        self.X = None
        self.y = None
        self.features = ['Open', 'High', 'Low', 'Close_diff', 'Rolling_mean_5',
                         'Rolling_std_5', 'EMA_10', 'RSI', 'MACD', 'Volume_scaled']

    @pytest.mark.parametrize("data", load_test_data(DATA_FILE_PATH, "datasheet"))
    def yahoofExtractData(self, Stock):
        # Get today's date
        today = datetime.now()

        # Calculate the date 5 years ago
        five_years_ago = today - relativedelta(years=5)

        # Download data using yfinance
        iDataset = yf.download(tickers=Stock, period="5y", interval="1d")

        # Save the dataset to a file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_dir = REPORT_PATH
        os.makedirs(self.output_dir, exist_ok=True)
        file_name = os.path.join(self.output_dir, f"{Stock}_data_{timestamp}.csv")
        iDataset.to_csv(file_name)
        print(f"Data successfully downloaded and saved to {file_name}.")
        return file_name  # Return the file path for further processing

    def dataclearning(self):
        load_test_data(DATA_FILE_PATH, "data")
