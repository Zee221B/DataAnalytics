from data_extraction import DataExtractor
from data_cleaning import DataCleaning
from database_utils import DatabaseConnector

database_connector = DatabaseConnector()
data_extractor = DataExtractor()
data_cleaning = DataCleaning()

s3_1987 = "s3://myflightsbucket/1987.csv"
s3_1989 = "s3://myflightsbucket/1989.csv"
s3_1990 = "s3://myflightsbucket/1990.csv"
s3_1991 = "s3://myflightsbucket/1991.csv"
s3_1992 = "s3://myflightsbucket/1992.csv"
s3_1993 = "s3://myflightsbucket/1993.csv"
s3_1994 = "s3://myflightsbucket/1994.csv"
s3_1995 = "s3://myflightsbucket/1995.csv"
s3_1996 = "s3://myflightsbucket/1996.csv"


my_flights_bucket = data_extractor.extract_from_s3(s3_1987, s3_1989, s3_1990, s3_1991, s3_1992, s3_1993, s3_1994, s3_1995, s3_1996)

