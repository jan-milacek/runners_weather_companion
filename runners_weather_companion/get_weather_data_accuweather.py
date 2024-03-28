import asyncio
import logging
from aiohttp import ClientError, ClientSession
from accuweather import (
    AccuWeather,
    ApiError,
    InvalidApiKeyError,
    InvalidCoordinatesError,
    RequestsExceededError,
)
import pandas as pd

logging.basicConfig(level=logging.DEBUG)



def get_accuweather_12_hour_forecast(latitude, longitude):
    loop =  asyncio.new_event_loop()
    result =  loop.run_until_complete(accuweather_load_12_hours(latitude, longitude))
    loop.close()
    df_accuweather = pd.json_normalize(result)
    df_accuweather['DateTime'] = pd.to_datetime(df_accuweather['DateTime']).dt.tz_localize(None)
    df_accuweather['Precipation.Value'] = df_accuweather['Rain.Value'] + df_accuweather['Snow.Value']
    df_accuweather = df_accuweather.set_index(['DateTime']).add_prefix('accuweather_')
    return df_accuweather

async def accuweather_load_12_hours(latitude, longitude):
    from . import API_keys
    accuweather_API_key = API_keys.accuweather_API_key
    async with ClientSession() as websession:
        try:
            accuweather = AccuWeather(
                accuweather_API_key,
                websession,
                latitude=latitude,
                longitude=longitude,
                language="en",
            )
            forecast_hourly = await accuweather.async_get_hourly_forecast(
                hours=12, metric=True
            )
        except (
            ApiError,
            InvalidApiKeyError,
            InvalidCoordinatesError,
            ClientError,
            RequestsExceededError,
        ) as error:
            print(f"Error: {error}")
        else:
            return(forecast_hourly)


