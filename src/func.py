# https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>
from ast import arg
import requests
import sys

def get_address(lat, lon, params):
    url='https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>'
    url.replace(f'lat=<value>', f'lat=<{lat}>')
    url.replace(f'lon=<value>', f'lon=<{lon}>')
    if params != "":
        url.replace(f'&<params>', f'&<{params}>')
    else:
        url.replace(f'&<params>', f'')
    response=requests.get(url)
    print(response)
    # content=response.json()
    # print(content)

if __name__=='__main__':
    lat=sys.argv[0]
    lon=sys.argv[1]
    params=""
    if len(sys.argv)>2:
        params=sys.argv[2]
    get_address(lat, lon, params)