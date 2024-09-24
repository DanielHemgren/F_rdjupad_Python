import logging
import os
from api import API
from datacleaner import DataCleaner
from datasaver import DataSaver

log_directory = 'logs'  # Hardcoded relative path for the log directory
os.makedirs(log_directory, exist_ok=True)  # Ensure the logs directory exists

logging.basicConfig(
    filename=os.path.join(log_directory, 'pipeline.log'),  # Hardcoded relative path for the log file
    format='[%(asctime)s][%(name)s] %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S', 
    level=logging.INFO)


logger = logging.getLogger(__name__)

def main():
    api = API()
    dc = DataCleaner()
    ds = DataSaver()

    logger.info('Startar data pipeline...')

    try:
        # Data fetched 
        data = api.fetch_data()

        # Data cleaned
        if not data.empty:
            cleaned_data = dc.clean_data(data, 'SP500')  # Adjust 'Close' based on your data

            # Data saved 
            ds.save_data(cleaned_data)
        else:
            logger.warning('Ingen data laddad')

    except Exception as e:
        logger.error(f'Ett fel uppstod under pipeline execution: {e}')

    logger.info('mini data pipeline klar')

if __name__ == "__main__":
    main()