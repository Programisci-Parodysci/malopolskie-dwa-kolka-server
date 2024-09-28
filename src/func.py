# https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>
from ast import arg
import requests
import sys
import asyncio
from geopy.geocoders import Nominatim
import json

app = Nominatim(user_agent="malopolskie_dwa_kola")

def get_address(lat, lon, params):
    url='https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>'
    url=url.replace(f'lat=<value>', f'lat={lat}')
    url=url.replace(f'lon=<value>', f'lon={lon}')
    url=url.replace(f'&<params>', f'')
    response=requests.get(url)
    content=response.content
    print(content)


def get_suggestions(letters):
    url='https://nominatim.openstreetmap.org/search?<params>'
    url=url.replace(f'<params>', f'q={letters}&layer=address')
    print(url)
    response=requests.get(url)
    content=response.content
    print(response)
    print(content)

def get_suggestions_photon(letters):
    '''zalecam podanie nazwy województwa po przecinku tzn. Lesser Poland Voivodeship'''
    url='https://photon.komoot.io/api/?<params>'
    url=url.replace(f'<params>', f'q={letters}')
    print(url)
    response=requests.get(url)
    content=response.content
    print(response)
    print(content)

if __name__=='__main__':
    # lat=sys.argv[1]
    # lon=sys.argv[2]
    # params=""
    # if len(sys.argv)>3:
    #     params=sys.argv[3]
    #     print('params:', params)
    # get_address(lat, lon, params)
    get_suggestions_photon('Kra, Lesser Poland Voivodeship')