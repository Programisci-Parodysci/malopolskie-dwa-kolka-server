# https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>
from ast import arg
import requests
import sys
import asyncio
from geopy.geocoders import Nominatim

app = Nominatim(user_agent="malopolskie_dwa_kola")

def get_address(lat, lon, params):
    url='https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>'
    url=url.replace(f'lat=<value>', f'lat={lat}')
    url=url.replace(f'lon=<value>', f'lon={lon}')
    url=url.replace(f'&<params>', f'')
    print(url)
    response=requests.get(url)
    print(response)
    content=response.content
    print(content)

if __name__=='__main__':
    lat=sys.argv[1]
    lon=sys.argv[2]
    params=""
    if len(sys.argv)>3:
        params=sys.argv[3]
        print('params:', params)
    get_address(lat, lon, params)