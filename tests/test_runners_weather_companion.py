#!/usr/bin/env python

"""Tests for `runners_weather_companion` package."""


import unittest

from runners_weather_companion.get_weather_data_met_no import get_met_no_12_hour_forecast
from runners_weather_companion.get_weather_data_accuweather import get_accuweather_12_hour_forecast

class TestRunners_weather_companion(unittest.TestCase):
    """Tests for `runners_weather_companion` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_met_no_API(self):
        result = get_met_no_12_hour_forecast(50.0874654,  14.4212535)
        assert 'met_no_data.instant.details.air_temperature' in result.columns
        assert 'met_no_data.instant.details.air_temperature' in result.columns
        assert 'met_no_data.instant.details.air_temperature' in result.columns
        assert 'met_no_data.instant.details.wind_speed' in result.columns
        assert 'met_no_data.instant.details.wind_speed' in result.columns
        assert 'met_no_data.instant.details.wind_speed' in result.columns
        assert 'met_no_data.next_1_hours.details.precipitation_amount' in result.columns
        assert 'met_no_data.next_1_hours.details.precipitation_amount' in result.columns
        assert 'met_no_data.next_1_hours.details.precipitation_amount' in result.columns


    def test_accuweather_API(self):
        result = get_accuweather_12_hour_forecast(50.0874654,  14.4212535)
        assert 'accuweather_Temperature.Value' in result.columns
        assert 'accuweather_Temperature.Value' in result.columns
        assert 'accuweather_Temperature.Value' in result.columns
        assert 'accuweather_Wind.Speed.Value' in result.columns
        assert 'accuweather_Wind.Speed.Value' in result.columns
        assert 'accuweather_Wind.Speed.Value' in result.columns
        assert 'accuweather_Precipation.Value' in result.columns
        assert 'accuweather_Precipation.Value' in result.columns
        assert 'accuweather_Precipation.Value' in result.columns


if __name__ == '__main__':
    unittest.main()
