import pandas as pd
import boto3 
import json

class DataExtractor():
     
    def retrieve_csv_data(self, database_connector, csv_path):
        master_df = pd.read_csv(csv_path, pages='all')
        master_df= pd.concat(pd.read_pdf(csv_path, pages='all'), ignore_index=True)
        print(len(master_df))
        return master_df