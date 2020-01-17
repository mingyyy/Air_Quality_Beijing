import requests
from mi import meteostat_key
from pprint import pprint
from datetime import datetime

key = meteostat_key
endpoint = 'https://api.meteostat.net/{VERSION}/{PACKAGE}/{METHOD}?{PARAMETERS}'


def search_station(city):
    '''
    :param city: city name
    :return: dictionary of the city
    '''
    url = f'https://api.meteostat.net/v1/stations/search?q={city}&key={key}'
    r = requests.get(url=url)
    data = r.json()
    if data:
        pprint(data)
        return f"Station ID of {city} is {data['data'][0]['id']}. "
    else:
        return "Sorry, something went wrong, please check your url."
# {'data': [{'country': 'CN', 'id': '54511', 'name': 'Beijing'}], 'meta': {}}


def station_metadata(station):
    '''
    :param station: station_id
    :return: meta information for station with inventory
    '''
    url = f'https://api.meteostat.net/v1/stations/meta?station={station}&inventory=1&key={key}'
    r = requests.get(url=url)
    data = r.json()
    if data:
        return data['data']
    else:
        return "Sorry, something went wrong, please check your url."

'''
data = 
{'data': {'country': {'code': 'CN', 'name': 'China'},
          'elevation': '55',
          'iata': 'PEK',
          'icao': 'ZBAA',
          'id': '54511',
          'inventory': {'daily': {'end': '2020-01-08', 'start': '1945-10-31'},
                        'hourly': {'end': '2020-01-22', 'start': '1945-10-31'},
                        'monthly': {'end': '2018', 'start': '1981'}},
          'latitude': '39.9333',
          'longitude': '116.2833',
          'name': 'Beijing',
          'region': '11',
          'time_zone': 'Asia/Shanghai',
          'wmo': '54511'},
 'meta': {}}
'''


def start_end_date(station, freq):
    '''
    :param station: station_id
    :return: meta information for station with inventory
    '''
    url = f'https://api.meteostat.net/v1/stations/meta?station={station}&inventory=1&key={key}'
    r = requests.get(url=url)
    data = r.json()
    if data:
        return data['data']['inventory'][freq]['start'], data['data']['inventory'][freq]['end']
    else:
        return "Sorry, something went wrong, please check your url."


def get_historical(freq, station, start, end):
    '''
    :param freq: hourly/daily/weekly in string format
    :param station: station id
    :param start: start date in format 'yyyy-mm-dd'
    :param end: end date in format 'yyyy-mm-dd'
    :return: list of dictionaries
    '''
    url = f'https://api.meteostat.net/v1/history/{freq}?station={station}&start={start}&end={end}&key={key}'
    r = requests.get(url=url)
    data = r.json()
    if data:
        return data['data']
    else:
        return "Sorry, something went wrong, please check your url."


if __name__ == '__main__':
    # print(search_station('Beijing'))
    start_date, end_date = start_end_date('54511', 'hourly')
    print(start_date, end_date)

    end = datetime.strptime(end_date, '%Y-%m-%d')
    if (datetime.now() - end).days > 0:
        print(end, type(end))
    else:
        print("end date is ahead!")

    # hist = get_historical('daily', '54511', end_date, end_date)
    # pprint(hist)

    # spark_json = sc.parallelize(hist)
    # spark_df = sqlContext.read.json(spark_json)
    # or
    # from pyspark.sql import Row
    # spark.createDataFrame(Row(**x) for x in hist).show(truncate=False)
