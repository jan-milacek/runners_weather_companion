import argparse
import os
import sys
import inquirer  # noqa
import requests
from . import API_keys
import get_weather_data_met_no
import get_weather_data_accuweather
import pandas as pd

sys.path.append(os.path.realpath("."))

def get_locations(city):

    url = "https://geocoding-by-api-ninjas.p.rapidapi.com/v1/geocoding"

    querystring = {"city": city}

    headers = {
        "X-RapidAPI-Key": API_keys.geocoding_by_API_ninjas,
        "X-RapidAPI-Host": "geocoding-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return(response.json())


def select_location(locations):
    questions = [
        inquirer.List(
            "selected_location",
            message="Select your location",
            choices=locations,
        ),
    ]
    selected_location = inquirer.prompt(questions)
    return(selected_location)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-city','--city_name', help='City name')
    args = parser.parse_args()
    if not args.city_name: city_name = input("Enter name of the city: ")
    else: city_name = args.city_name

    locations = get_locations(city_name)
    location = select_location(locations)

    df_met_no = get_weather_data_met_no.get_met_no_12_hour_forecast(location['selected_location']['latitude'], location['selected_location']['longitude'])
    df_accuweather = get_weather_data_accuweather.get_accuweather_12_hour_forecast(location['selected_location']['latitude'], location['selected_location']['longitude'])
    df_merged = pd.merge(df_met_no, df_accuweather, left_index=True, right_index=True).filter(
        ['met_no_data.instant.details.air_temperature', 'met_no_data.instant.details.wind_speed',
         'met_no_data.next_1_hours.details.precipitation_amount', 'accuweather_Temperature.Value',
         'accuweather_Wind.Speed.Value', 'accuweather_Precipation.Value'])
    df_merged['temperature.optimistic'] = df_merged[['met_no_data.instant.details.air_temperature', 'accuweather_Temperature.Value']].values.max(1)
    df_merged['temperature.pesimistic'] = df_merged[['met_no_data.instant.details.air_temperature', 'accuweather_Temperature.Value']].values.min(1)
    df_merged['temperature.average'] = df_merged[['met_no_data.instant.details.air_temperature', 'accuweather_Temperature.Value']].mean(axis=1)

    df_merged['wind_speed.optimistic'] = df_merged[['met_no_data.instant.details.wind_speed', 'accuweather_Wind.Speed.Value']].values.min(1)
    df_merged['wind_speed.pesimistic'] = df_merged[['met_no_data.instant.details.wind_speed', 'accuweather_Wind.Speed.Value']].values.max(1)
    df_merged['wind_speed.average'] = df_merged[['met_no_data.instant.details.wind_speed', 'accuweather_Wind.Speed.Value']].mean(axis=1)

    df_merged['precipation.optimistic'] = df_merged[['met_no_data.next_1_hours.details.precipitation_amount', 'accuweather_Precipation.Value']].values.max(1)
    df_merged['precipation.pesimistic'] = df_merged[['met_no_data.next_1_hours.details.precipitation_amount', 'accuweather_Precipation.Value']].values.min(1)
    df_merged['precipation.average'] = df_merged[['met_no_data.next_1_hours.details.precipitation_amount', 'accuweather_Precipation.Value']].mean(axis=1)
    print(df_merged)

if __name__ == "__main__":
    main()
    """Main module."""
