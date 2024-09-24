import sys
import os
import pytest
from unittest.mock import patch
import pandas as pd

# to find api.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api import API  # Assuming your API class is in api.py

api = API()

# Test case 1: Data loads 
@patch('pandas.read_excel')
def test_fetch_data_success(mock_read_excel):
    # Mock successful data
    mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    mock_read_excel.return_value = mock_df
    
    result = api.fetch_data()
    
    # things to assert
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert result.shape == (2, 2)

# Test case 2: FileNotFoundError
@patch('pandas.read_excel')
def test_fetch_data_file_not_found(mock_read_excel):
    # Simulate FileNotFoundError
    mock_read_excel.side_effect = FileNotFoundError
    
    result = api.fetch_data()
    
    # things to assert
    assert isinstance(result, pd.DataFrame)
    assert result.empty







