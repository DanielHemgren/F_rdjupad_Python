import logging
import pandas as pd

data1 = 'SP500.xls'

class API:
    #Class created to fetch data
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def fetch_data(self) -> pd.DataFrame:
        self.logger.info('mottar data...')
        try:
            df = pd.read_excel(data1)  # to make sure data is in right location
            self.logger.info('Datan mottas')
            return df
        except FileNotFoundError:
            self.logger.error('Kan ej finna data')
            return pd.DataFrame()  # Return empty DataFrame if the data is missing
        except Exception as e:
            self.logger.error(f'Ett fel uppstod när data mottogs: {e}')
            return pd.DataFrame()  # Return an empty DataFrame if other error occurs





