import requests
from mi import meteostat_key
from pprint import pprint

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
        pprint(data)
    else:
        return "Sorry, something went wrong, please check your url."

'''
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


if __name__ == '__main__':
    print(search_station('Beijing'))
    station_metadata('54511')
