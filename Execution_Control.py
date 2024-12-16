import pytest
import time
import os
import pandas as pd



@pytest.fixture(scope="session")
def config():
    # Configuration details for the base URL
    return {
        "base_url": "https://finance.yahoo.com/"  # Replace with your app's URL
    }
if __name__ == "__main__":
    pass