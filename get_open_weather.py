# !/usr/bin/env python3
"""
Gets current weather data for a given city.
"""

import logging
import sys
import json
import requests
from geopy.geocoders import Nominatim
import os

API_ID = os.getenv("OPEN_WEATHER_APPID")


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug(f"Open Weather Map API ID: {API_ID}")

def get_coordinates(city):
    """Gets coordinates to a city."""
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(city, timeout=5)
    if location:
        return location
    else:
        print("Coordinates not found for the given city.")
        return None


# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: get_open_weather.py city_name, state')
    sys.exit()

city = ' '.join(sys.argv[1:])
logging.debug(city)

location = get_coordinates(city)

lat = location.latitude
lon = location.longitude
city_address = location.address

units = 'imperial'
url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units={units}&appid={API_ID}'

response = requests.get(url)
response.raise_for_status()

weather_data = json.loads(response.text)

temp = weather_data['current']['temp']
feels_like = weather_data['current']['feels_like']

main = weather_data['current']['weather'][0]['main']
description = weather_data['current']['weather'][0]['description']

header = f'{city_address}'
report = f'Current conditions are {description} wit a temperature of {temp} F that feels like {feels_like} F.'

separator = 113
# if len(report) > len(header):
    # separator = len(report)
# else:
    # separator = len(header)
print('=' * separator)
print(r"""
██╗    ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗     ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
██║    ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗    ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝    ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   
██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗    ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   
╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║    ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   
 ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝    
""")
print(r"""
,--.::::::::::::::::::::::::::::::::::::....:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    )::::::::::::::::::::::::::::::::..      ..::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  _'-. _:::::::::::::::::::::::::::..   ,--.   ..::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 (    ) ),--.::::::::::::::::::::::.   (    )   .::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
             )-._::::::::::::::::::..   `--'   ..::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
_________________):::::::::::::::::::..      ..::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::....:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!||!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
""")

print(header)
print('=' * separator)
print(report)
print('=' * separator)
print()
