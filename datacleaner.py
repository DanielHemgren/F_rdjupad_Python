import logging
import pandas as pd

class DataCleaner:
    # Class to clean data
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def clean_data(self, data: pd.DataFrame, column: str = 'SP500') -> pd.DataFrame:
        self.logger.info(f'bearbetar data i kolumn: {column}...')

        if data.empty:
            self.logger.warning('Ingen data att bearbeta..')
            return pd.DataFrame()  # empty DataFrame if no data

        # null values droppas 
        data = data.dropna(subset=[column])
        
        # only rows with valid float values included
        cleaned_data = data[data[column].apply(lambda x: isinstance(x, float))]

        self.logger.info(f'bearbetad data: {cleaned_data}')
        return cleaned_data






