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

### Extraction

Most of the efforts are dedicated to sourcing data from various public open data projects. 
1. From the meteostat API, we could have the historical hourly/daily/weekly weather records based on synoptical observations and METAR data. 
Note: gaps in the time series are filled with statistically optimised MOSMIX model data.

Given station id, start date, end date, time zone and time format, we get the following data points:
`temperature`, `dewpoint`, `humidity`, `precipitation`, `precipitation_3`, `precipitation_6`, `snowdepth`, `windspeed`, 
`peakgust`, `winddirection`, `pressure`, `condition`

Currently, the hourly dataset contains records from *1945-10-31* to *2020-01-08*. 

2. 

### Transformation

### Load

### Analysis


