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
        content=response.json()
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
    return (f'{location.latitude},{location.longitude}')

def get_readable_adresses(num_of_adresses, content):
    '''zwraca listę adresów w formacie: ulica, miasto, województwo'''
    addresses=[]
    for feature in content["features"][:num_of_adresses]:
        street=feature["properties"].get("street", "")
        city=feature["properties"].get("city", "")
        state=feature["properties"].get("state", "")
        name=feature["properties"].get("name", "")
        address = ', '.join([part for part in [street, city, state, name] if part])
        addresses.append(address)
    return addresses

if __name__=='__main__':
    json_content=get_suggestions_photon('Kra, Lesser Poland Voivodeship')
    print(json_content)
    print(get_readable_adresses(5, json_content))
