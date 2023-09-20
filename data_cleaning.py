import pandas as pd
import numpy as np

class DataCleaning:
    @staticmethod
    def clean_csv_data(self,df,df2,df3,df4,df5,df6,df7,df8,df9):
    

    # Removes any columns that contain NULL or NA values in all of their records.
        df = df.dropna(axis=1, how='all')
        df2 = df2.dropna(axis=1, how='all')
        df3 = df3.dropna(axis=1, how='all')
        df4 = df4.dropna(axis=1, how='all')
        df5 = df5.dropna(axis=1, how='all')
        df6 = df6.dropna(axis=1, how='all')
        df7 = df7.dropna(axis=1, how='all')
        df8 = df8.dropna(axis=1, how='all')
        df9 = df9.dropna(axis=1, how='all')
   
    # Replaces remaining null values with zero
        df2 = df.fillna(0)
        df3 = df2.fillna(0)
        df4 = df3.fillna(0)
        df5 = df4.fillna(0)
        df6 = df5.fillna(0)
        df7 = df6.fillna(0)
        df8 = df7.fillna(0)
        df9 = df8.fillna(0)
        df10 = df9.fillna(0)
    
   # integrates all of the dataframes together into one master dataframe.
        dfs = [df, df2, df3,df4,df5,df6,df7,df8,df9]
        master_df = pd.concat(dfs, axis=1)  

   # Displays the resulting master DataFrame
        print("Master DataFrame:")
        print(master_df)

    #  exports the final master dataframe into one file called combined_data.csv.
        master_df.to_csv('combined_data.csv', index=False)  # Set index=False to exclude row numbers in the CSV
        print("Master DataFrame exported to 'combined_data.csv'.")
     

        return master_df


