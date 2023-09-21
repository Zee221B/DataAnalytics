import pandas as pd
import numpy as np

class DataCleaning:
    

    def __init__(self):
       self.csv_list = [r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1987.csv", 
                   r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1989.csv",
                   r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1990.csv",
                   r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1991.csv",
                   r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1992.csv",
                   r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1993.csv",
                   r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1994.csv",
                   r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1995.csv",
                   r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1996.csv"] 

    # reads csv and creates a dataframe
    # def clean_csv_data(self,df_list):
    #     pd_list = []
    #     for df in df_list: 
    #         master_df = pd.read_csv(df)
    #         pd_list.append(master_df)
        
    #     master_df = pd.concat(pd_list) 
    #     return master_df
    
   #returns a clean df
    def clean_df(self, df):
        df = df.dropna(axis=1, how='all')
        df.fillna(0,inplace=True)
        #make all columns the same type in every dataframe
        return df
    
    #takes a clean data frame puts it in a list
    def create_and_clean_df(self):
        clean_df_list = []
        for csv_path in self.csv_list:
            df = pd.read_csv(csv_path)
            clean_df_list.append(self.clean_df(df))
        return clean_df_list
    
    def create_master_df(self):
         master_df = pd.concat(self.create_and_clean_df()) 
         return master_df

    def export_df_to_csv(self):
         export_df = self.create_master_df()
         export_df.to_csv("combined_data_csv",index=False)
         print("Master DataFrame exported to 'combined_data.csv'.")

data_cleaning = DataCleaning()
data_cleaning.export_df_to_csv()










#copies combined data csv to your S3 bucket
#aws s3 cp combined_data.csv s3://myflightsbucket/combined_data.csv