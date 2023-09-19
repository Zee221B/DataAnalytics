import pandas as pd
import boto3 
import json

class DataExtractor():
    def extract_from_s3(self, s3_1987, s3_1989, s3_1990, s3_1991, s3_1992, s3_1993, s3_1994, s3_1995, s3_1996):
        """extract data from an s3 bucket and returns a pandas DataFrame"""

        # Split the s3 address into its components 
        bucket, key = s3_1987.replace('s3://', '').split('/', 1)
        bucket, key = s3_1989.replace('s3://', '').split('/', 1)
        bucket, key = s3_1990.replace('s3://', '').split('/', 1)
        bucket, key = s3_1991.replace('s3://', '').split('/', 1)
        bucket, key = s3_1992.replace('s3://', '').split('/', 1)
        bucket, key = s3_1993.replace('s3://', '').split('/', 1)
        bucket, key = s3_1994.replace('s3://', '').split('/', 1)
        bucket, key = s3_1995.replace('s3://', '').split('/', 1)
        bucket, key = s3_1996.replace('s3://', '').split('/', 1)

        # Create a client accessing the 3 bucket and informing boto3 that we itnent to use a s3 bucket 

        s3 = boto3.client('s3')

        # Download the file from s3
        response = s3.get_object(Bucket = bucket, Key = key)
        body = response['Body']

        # Read the contents of the file into a pandas DataFrame
        my_flights_bucket = pd.read_csv(body)

        return my_flights_bucket