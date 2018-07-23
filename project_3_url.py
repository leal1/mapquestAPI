# ANDY LE 92855131

import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = 'nwa23KMI1UA9hfZTbgDk3WVQfsyGkQ4C'
ELEVATION_BASE = 'http://open.mapquestapi.com/elevation/v1/profile?'
DIRECTION_BASE = 'http://open.mapquestapi.com/directions/v2/route?'

def build_direction_url(locations: ['locations'], ) -> str:
    '''
    Display, and builds and returns
    a URL that can be used to ask the MapQuest API for
    information about directions, distance, time, lattiude,
    and longitude
    '''

    query_parameters = [
            ('key', MAPQUEST_API_KEY), ('from', locations[0])]

    for n in range(len(locations) - 1):
        query_parameters.append(('to', locations[n+1]))
        
    return DIRECTION_BASE + urllib.parse.urlencode(query_parameters)

def build_elevation_url(latLng: 'str of lattitudes and longitudes') -> str:
    '''
    Display, and builds and returns
    a URL that can be used to ask the MapQuest API for
    information about elevation
    '''
    query_parameters = [
            ('key', MAPQUEST_API_KEY), ('shapeFormat', 'raw'),
            ('latLngCollection', latLng), ('unit', 'f')]
        
    return ELEVATION_BASE + urllib.parse.urlencode(query_parameters)

def get_result(url: str) -> dict:
    '''
    This function takes a URL and returns a Python dictionary representing the
    parsed JSON response.
    '''
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')


        return json.loads(json_text)
 

    finally:

        if response != None:
            response.close()


    
