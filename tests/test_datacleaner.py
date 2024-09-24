import sys
import os
import pytest
import pandas as pd

# to find datacleaner.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datacleaner import DataCleaner  # Import  DataCleaner class

# Initialize DataCleaner instance
dc = DataCleaner()

def test_clean_data_returns_dataframe():
    # mock DataFrame with float values as input (should work)
    mock_data = pd.DataFrame({'SP500': [100.0, 200.0, 300.0]})
    
    # Test that clean_data returns a DataFrame after processing
    result = dc.clean_data(mock_data)

    # Print the result DataFrame
    print(result)  
    
    # Assertions 
    assert isinstance(result, pd.DataFrame)  # Ensure DataFrame is result
    assert not result.empty  # Check if  DataFrame contains data







