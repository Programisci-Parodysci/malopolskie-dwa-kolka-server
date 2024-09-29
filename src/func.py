# https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>
from ast import arg
import requests
import sys
import asyncio
from geopy.geocoders import Nominatim
import json
from log import logger

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
        logger.error(e)
        return ""
    return content


def get_suggestions(letters):
    url='https://nominatim.openstreetmap.org/search?<params>'
    url=url.replace(f'<params>', f'q={letters}&layer=address')
    try:
        response=requests.get(url)
        content=response.content
    except Exception as e:
        logger.error(e)
        return ""
    return content

def get_suggestions_photon(letters):
    '''zalecam podanie nazwy województwa po przecinku tzn. Lesser Poland Voivodeship'''
    logger.info(f'letters: {letters}')
    url='https://photon.komoot.io/api/?<params>'
    url=url.replace(f'<params>', f'q={letters}')
    logger.debug(f'url: {url}')
    try:
        response=requests.get(url)
        content=response.content
    except Exception as e:
        logger.error(e)
        return ""
    return content

def get_coordinates_from_address(address):
    '''zwraca krotkę (lat, lon)'''
    logger.info(f'address: {address}')
    try:
        location = app.geocode(address)
        logger.debug(f'location: {location}')
    except Exception as e:
        logger.error(e)
        return "", ""
    return location.latitude, location.longitude

if __name__=='__main__':
    # lat=sys.argv[1]
    # lon=sys.argv[2]
    # params=""
    # if len(sys.argv)>3:
    #     params=sys.argv[3]
    #     print('params:', params)
    # get_address(lat, lon, params)
    get_coordinates_from_address('Kraków, Lesser Poland Voivodeship')