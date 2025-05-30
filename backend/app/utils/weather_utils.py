import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
import requests
from app.settings import settings

#----------------------OpenMeteoSetUp-----------------------------------------------
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)
#-----------------------------------------------------------------------------------


def get_coords(city: str) -> tuple[str, str]:
    """
    Takes city as param and returns its latitude and longitude as a tuple of strings
    :param city: 
    :return tuple[str, str]; 
    """
    data = requests.get(f"https://catalog.api.2gis.com/3.0/items/geocode?q={city}&fields=items.point&key={settings.weather.api}")
    data = data.json()
    base = data['result']['items'][0]['point']
    lat = str(base['lat'])
    lon = str(base['lon'])
    return lat,lon

def get_weather_by_city(coords: tuple[str, str]):
    """
    Gets weather data for specified coordinates
    :param coords: tuple of (latitude, longitude)
    :return: dictionary with time and temperature data
    """
    params = {
        "latitude": coords[0],
        "longitude": coords[1],
        "hourly": "temperature_2m"
    }
    responses = openmeteo.weather_api(settings.weather.base_forecast_url, params=params)
    response = responses[0]
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_data = {
        "time": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left"
        ).strftime("%Y-%m-%d %H:%M").tolist(), 
        "temperature_2m": hourly_temperature_2m.tolist()
    }
    return hourly_data

    
