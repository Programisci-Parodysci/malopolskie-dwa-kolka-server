# https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>
from ast import arg
import requests
import sys
import asyncio
from geopy.geocoders import Nominatim
import json
# from logs import logger

app = Nominatim(user_agent="malopolskie_dwa_kola")

def get_address(lat, lon, params):
    url='https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>'
    url=url.replace(f'lat=<value>', f'lat={lat}')
    url=url.replace(f'lon=<value>', f'lon={lon}')
    url=url.replace(f'&<params>', f'')
    try:
        response=requests.get(url)
        content=response.content
    except Exception as e:
        # logger.error(e)
        return ""
    return content


def get_suggestions(letters):
    url='https://nominatim.openstreetmap.org/search?<params>'
    url=url.replace(f'<params>', f'q={letters}&layer=address')
    try:
        response=requests.get(url)
        content=response.content
    except Exception as e:
        # logger.error(e)
        return ""
    return content

def get_suggestions_photon(letters):
    '''zalecam podanie nazwy województwa po przecinku tzn. Lesser Poland Voivodeship'''
    # logger.info(f'letters: {letters}')
    url='https://photon.komoot.io/api/?<params>'
    url=url.replace(f'<params>', f'q={letters}')
    # logger.debug(f'url: {url}')
    try:
        response=requests.get(url)
        content=response.content
    except Exception as e:
        # logger.error(e)
        return ""
    return content

def get_coordinates_from_address(address):
    '''zwraca krotkę (lat, lon)'''
    # logger.info(f'address: {address}')
    try:
        location = app.geocode(address)
        # logger.debug(f'location: {location}')
    except Exception as e:
        # logger.error(e)
        return ""
    return (f'{location.latitude}, {location.longitude}')

if __name__=='__main__':
    print(get_suggestions_photon('Krak, Lesser Poland Voivodeship'))