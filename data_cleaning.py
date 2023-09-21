import pandas as pd
import numpy as np

class DataCleaning:
    

    def __init__(self):
        pass
        
    
    def clean_csv_data(self,df_list):
        pd_list = []
        for df in df_list: 
            master_df = pd.read_csv(df)
            pd_list.append(master_df)
        
        master_df = pd.concat(pd_list) 
        return master_df
    
    
df = r'C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1987.csv'
df2 = r'C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1989.csv'
df3 = r'C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1990.csv'
df4 = r'C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1991.csv'
df5 = r'C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1992.csv'
df6 = r'C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1993.csv'
df7 = r'C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1994.csv'
df8 = r'C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1995.csv'
df9 = r'C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1996.csv'


dfs = [df,df2,df3,df4,df5,df6,df7,df8,df9]

#convert dfs list to a dataframe

dfs_final = pd.DataFrame(dfs)


# Removes any columns that contain NULL or NA values in all of their records.
dfs_final = dfs_final.dropna(axis=1, how='all')

# Replaces remaining null values with zero
dfs_final = dfs_final.fillna(0)

dc = DataCleaning()
#print(dc.clean_csv_data(dfs))

# exports the final master dataframe into one file called combined_data.csv.
dfs_final.to_csv('combined_data.csv', index=False)  # Set index=False to exclude row numbers in the CSV
print("Master DataFrame exported to 'combined_data.csv'.")


# Removes any columns that contain NULL or NA values in all of their records.
#df = df.dropna(axis=1, how='all')
#df2 = df2.dropna(axis=1, how='all')
#df3 = df3.dropna(axis=1, how='all')
#df4 = df4.dropna(axis=1, how='all')
#df5 = df5.dropna(axis=1, how='all')
#df6 = df6.dropna(axis=1, how='all')
#df7 = df7.dropna(axis=1, how='all')
#df8 = df8.dropna(axis=1, how='all')
#df9 = df9.dropna(axis=1, how='all')


# Replaces remaining null values with zero
#df2 = df.fillna(0)
#df3 = df2.fillna(0)
#df4 = df3.fillna(0)
#df5 = df4.fillna(0)
#df6 = df5.fillna(0)
#df7 = df6.fillna(0)
#df8 = df7.fillna(0)
#df9 = df8.fillna(0)
#df10 = df9.fillna(0)
    


# Displays the resulting master DataFrame
#print("Master DataFrame:")
#print(master_df)


     
aws s3 cp combined_data.csv s3://myflightsbucket/combined_data.csv

