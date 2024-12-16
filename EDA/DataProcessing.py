import os
import pandas as pd
import yfinance as yf
from Execution_Control import DATA_FILE_PATH
from Utilities.data_loader import load_test_data
import pytest

class DataProcessing:
        def __init__(self, ticker, start_date, end_date):
            self.ticker = ticker
            self.start_date = start_date
            self.end_date = end_date
            self.data = None
            self.stockname=None
            self.X = None
            self.y = None
            self.features = ['Open', 'High', 'Low', 'Close_diff', 'Rolling_mean_5',
                             'Rolling_std_5', 'EMA_10', 'RSI', 'MACD', 'Volume_scaled']

        @pytest.mark.parametrize("data", load_test_data(DATA_FILE_PATH, "datasheet"))
        def extractdata(self):
            self.data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
            #Yahoo finance only adds these many values by default hence feature engineering needed to meet the CA requirement
            self.data = self.data[['Open', 'High', 'Low', 'Close', 'Volume']]

        def dataclearning(self):
            load_test_data(DATA_FILE_PATH,"data")
