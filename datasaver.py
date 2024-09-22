import logging
import pandas as pd
import sqlite3  # Import SQLite library

class DataSaver:
    #Class for saving the data to SQL
    def __init__(self, db_path: str = 'database.db') -> None:
        self.logger = logging.getLogger(__name__)
        self.db_path = db_path  # Path to SQLite database file

    def save_data(self, data: pd.DataFrame, table_name: str = 'cleaned_data') -> None:
        if data.empty:
            self.logger.warning('Ingen data att spara')
            return
        
        try:
            #SQLite database connected or created 
            with sqlite3.connect(self.db_path) as conn:
                # DataFrame saved to SQL
                data.to_sql(table_name, conn, if_exists='replace', index=False)
                self.logger.info(f'Data sparat till table {table_name} i databas {self.db_path}.')
        except Exception as e:
            self.logger.error(f':Ett fel uppstod vid sparande till SQL {e}')




