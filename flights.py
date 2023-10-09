import numpy as np
import pandas as pd



    

csv_list = [r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1987.csv",
            r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1989.csv",
            r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1990.csv",
            r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1991.csv",
            r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1992.csv",
            r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1993.csv",
            r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1994.csv",
            r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1995.csv",
            r"C:\Users\zbe17\Desktop\AiCore_Projects\DataAnalytics\FlightsCSV\1996.csv"] 

def clean_df(df):
    df.fillna(0,inplace=True)
    df['Distance'] = df['Distance'].astype('float32')
    df ['Year'] = df['Year'].astype('int32')
    df ['Month'] = df['Month'].astype('int32')
    df ['DayofMonth'] = df['DayofMonth'].astype('int32')
    df ['DayOfWeek'] = df['DayOfWeek'].astype('int32')
    df ['DepTime'] = df['DepTime'].astype('float32')
    df ['CRSDepTime'] = df['CRSDepTime'].astype('int32')
    df ['ArrTime'] = df['ArrTime'].astype('float32')
    df ['CRSArrTime'] = df['CRSArrTime'].astype('int32')
    df ['UniqueCarrier'] = df['UniqueCarrier'].astype(object)
    df ['FlightNum'] = df['FlightNum'].astype('int32')
    df ['TailNum '] = df['TailNum'].astype(object)
    df ['ActualElapsedTime'] = df['ActualElapsedTime'].astype('float32')
    df ['CRSElapsedTime'] = df['CRSElapsedTime'].astype('float32')
    df ['AirTime'] = df['AirTime'].astype('float32')
    df ['ArrDelay'] = df['ArrDelay'].astype('float32')
    df ['DepDelay'] = df['DepDelay'].astype('float32')
    df ['Origin'] = df['Origin'].astype(object)
    df ['Dest'] = df['Dest'].astype(object)
    df ['TaxiIn '] = df['TaxiIn'].astype('int32')
    df ['TaxiOut'] = df['TaxiOut'].astype('int32')
    df ['Cancelled'] = df['Cancelled'].astype('int32')
    df ['Diverted'] = df['Diverted'].astype('int32')
    return df

def create_and_clean_df():
    clean_df_list = []
    for csv_path in csv_list:
        df = pd.read_csv(csv_path, nrows=30000)
        clean_df_list.append(clean_df(df))
        
    return clean_df_list

def create_master_df():
    master_df = pd.concat(create_and_clean_df()) 
    return master_df

def export_df_to_csv():
    export_df = create_master_df()
    export_df.to_csv("combined_data.csv",index=False)
    print("Master DataFrame exported to 'combined_data.csv'.")

export_df_to_csv()





