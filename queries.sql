# Milestone Task 4
CREATE TABLE flights (
	id serial PRIMARY KEY,
    Year INTEGER,
	Month INTEGER,
	DayofMonth INTEGER,
	DayOfWeek INTEGER,
	DepTime FLOAT,
	CRSDepTime INTEGER,
	ArrTime FLOAT,
	CRSArrTime INTEGER,
	UniqueCarrier OBJECT,
	FlightNum INTEGER,
	TailNum OBJECT,
	ActualElapsedTime FLOAT,
	CRSElapsedTime FLOAT,
	AirTime FLOAT,
	ArrDelay FLOAT,
	DepDelay FLOAT,
	Origin OBJECT,
	Dest OBJECT,
	Distance FLOAT,
	TaxiIn INTEGER,
	TaxiOut INTEGER,
	Cancelled INTEGER,
	CancellationCode OBJECT,
	Diverted INTEGER,
	CarrierDelay OBJECT,
	WeatherDelay OBJECT,
	NASDelay OBJECT,
	SecurityDelay OBJECT, 
	LateAircraftDelay OBJECT,
	TailNum OBJECT,
	TaxiIn OBJECT,
);

Milestone Task 5:
"Using SQL statements in pgAdmin4, explore the data in the flights table:"

1. Execute a SELECT statement and limit your results to 100 records. How many columns do you see?

SELECT *
FROM flights
LIMIT 100;

I see all 31 columns


2.How many total records does the table contain? 

SELECT count(*)
FROM flights;

270000 

3. Does it have the same number of records as those in the combined_data.csv file?

Yes!

4. Which year had the most number of total inbound and outbound flights? 




5.Which country is the most popular destination for flights?


