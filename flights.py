from data_extraction import DataExtractor
from data_cleaning import DataCleaning
from database_utils import DatabaseConnector

database_connector = DatabaseConnector()
data_extractor = DataExtractor()
data_cleaning = DataCleaning()

csv_path  = r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV"



master_df = data_extractor.retrieve_csv_data(database_connector, csv_path)



cleaned_master_df = data_cleaning.clean_csv_data(master_df)

