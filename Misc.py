#helpful tips 

# ctrl / to hash and unhash multiple lines 
# a good idea to keep a record of all your completed queries in a .sql file in vscode though
#that way you can upload them to your repo with the rest of your code

# space for unused code


from database_utils import DatabaseConnector 
from database_utils import DataExtractor
from database_utils import DataCleaning

database_connector = DatabaseConnector()
data_extractor = DataExtractor()
data_cleaning = DataCleaning()


#flights.py 

#from data_extraction import DataExtractor
#from data_cleaning import DataCleaning
#from database_utils import DatabaseConnector

#database_connector = DatabaseConnector()
#data_extractor = DataExtractor()
#data_cleaning = DataCleaning()

#csv_path  = r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV"



#master_df = data_extractor.retrieve_csv_data(database_connector, csv_path)


DataCleaning.py



#print(dfs)

# Removes any columns that contain NULL or NA values in all of their records.

#df2 = df2.dropna(axis=1, how='all')
#df3 = df3.dropna(axis=1, how='all')
#df4 = df4.dropna(axis=1, how='all')
#df5 = df5.dropna(axis=1, how='all')
#df6 = df6.dropna(axis=1, how='all')
#df7 = df7.dropna(axis=1, how='all')
#df8 = df8.dropna(axis=1, how='all')
#df9 = df9.dropna(axis=1, how='all')

# Replaces remaining null values with zero

#df3 = df2.fillna(0)
#df4 = df3.fillna(0)
#df5 = df4.fillna(0)
#df6 = df5.fillna(0)
#df7 = df6.fillna(0)
#df8 = df7.fillna(0)
#df9 = df8.fillna(0)
#df10 = df9.fillna(0)

#converts my list into a dataframe
# dfs_final = pd.DataFrame(dfs)

# # Removes any columns that contain NULL or NA values in all of their records.
# dfs_final= dfs.dropna(axis=1, how='all')

# # Replaces remaining null values with zero
# dfs_final = dfs.fillna(0)

# dc = DataCleaning()
# print(dc.clean_csv_data(dfs))

# # exports the final master dataframe into one file called combined_data.csv.
# dfs.to_csv('combined_data.csv', )  
# # Set index=False to exclude row numbers in the CSV


   # reads csv and creates a dataframe
    # def clean_csv_data(self,df_list):
    #     pd_list = []
    #     for df in df_list: 
    #         master_df = pd.read_csv(df)
    #         pd_list.append(master_df)
        
    #     master_df = pd.concat(pd_list) 
    #     return master_df