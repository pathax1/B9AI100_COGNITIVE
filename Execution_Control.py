import pytest
import os
from EDA.DataProcessing import DataManager
from Utilities.data_loader import load_test_data
from config import DATA_FILE_PATH

@pytest.mark.parametrize("data", load_test_data(DATA_FILE_PATH, "datasheet"))
def ExtractData(data):
    iData = DataManager()
    iData.yahoofExtractData(data["Stock"])  # Pass Stock to the DataManager method

if __name__ == "__main__":
    # Run the data extraction
    ExtractData()
