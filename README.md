# Air_Quality_Beijing

### Table of Content
1. [Objective](#objective)
2. [Data Source](#data-source)
3. [Overview](#overview)
4. [Extraction](#extraction)
5. [Transformation](#transformation)
6. [Load](#load)
7. [Analysis](#analysis)

### Objective
Building a data pipeline from public sources to get insight into Beijing's Air Quality.

### Data Source
1. [Historical weather data](https://api.meteostat.net/#introduction) for cities in or near Beijing from meteostat JSON API.
Note that API key is needed and free account has access limit, up to 200 calls per key an hour.

2. [Beijing Multi-Site Air-Quality Data Data Set](https://archive.ics.uci.edu/ml/datasets/Beijing+Multi-Site+Air-Quality+Data), 
originally from Center for Statistical Science, Peking University.

3. [Beijing Air Quality Index (AQI) Data Set](https://datahub.ckan.io/dataset/610fb217-0499-40e7-b53f-a50c9b02b98f/resource/772b62d8-0847-4104-ad97-ceac7fb0438d/download/beijing-aqm.txt)
from datahub

### Overview
Based on the current available data sets, we have decided on the following pipeline: extraction, load, transformation (ETL in short). 
After loading the three data sets, transformation is needed to make sure the data sets are cleaned, merged and casted into the 
right formats for further analysis which is mostly likely includes prediction of air quality in Beijing. 
#### Pipeline



#### Technology
As seen in the above chart, the following technologies are chosen: Python, Spark, Redshift, Airflow.

### Extraction

Most of the efforts are dedicated to sourcing data from various public open data projects. 
#### Source 1. meteostat API
From the meteostat API, we could have the historical hourly/daily/weekly weather records based on synoptical observations and METAR data. 
Note: gaps in the time series are filled with statistically optimised MOSMIX model data.

Given station id, start date, end date, time zone and time format, we get the following data points:
`temperature`, `dewpoint`, `humidity`, `precipitation`, `precipitation_3`, `precipitation_6`, `snowdepth`, `windspeed`, 
`peakgust`, `winddirection`, `pressure`, `condition`

Currently, the hourly dataset contains records from *1945-10-31* to *2020-01-08*. 

#### Source 2. CMA weather station Data
Based on the description at the website, We hve the Data Set and Attribute information for the well-defined data.
Since this is a one time historical clean data set, the idea here is to download the zip file to HDFS for further transformation

This data set includes hourly air pollutants data from 12 nationally-controlled air-quality monitoring sites. 
The air-quality data are from the Beijing Municipal Environmental Monitoring Center. 
The meteorological data in each air-quality site are matched with the nearest weather station from the China Meteorological Administration (CMA). 
The time period is from March 1st, 2013 to February 28th, 2017. Missing data are denoted as NA.

Attribute | Explanation
--- |  ---
No | row number
year | year of data in this row 
month | month of data in this row 
day | day of data in this row 
hour | hour of data in this row 
PM2.5 | PM2.5 concentration (ug/m^3) 
PM10 | PM10 concentration (ug/m^3) 
SO2 | SO2 concentration (ug/m^3) 
NO2 | NO2 concentration (ug/m^3) 
CO | CO concentration (ug/m^3) 
O3 | O3 concentration (ug/m^3) 
TEMP | temperature (degree Celsius) 
PRES | pressure (hPa) 
DEWP | dew point temperature (degree Celsius) 
RAIN | precipitation (mm) 
wd | wind direction 
WSPM | wind speed (m/s) 
station | name of the air-quality monitoring site

#### Source 3. AQI
 
This dataset could be downloaded directly in text format, containing hourly AQI (air quality index) reading starting 
from 2010-03-01 to 2016-05-31.

#### Error Handling
As an important part of the extraction effort, especially in production, error handling is of high importance. 
Here are a few aspects, we need to consider:
1. Data is not available at the given URL.
2. Access issue due to lack of authority, wrong(out-dated) API key or any other unforeseeable reasons.
3. Data is not loaded correctly, e.g. incorrect format, wrong columns, displaced information etc.
4. 

### Transformation

After loading three datasets from their respective resources, we have to merge the data in a meaningful fashion to 
provide the most complete and reasonable dataset for further analysis. 

### Load

### Analysis


