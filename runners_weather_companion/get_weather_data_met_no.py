from metno_locationforecast import Place, Forecast
import pandas as pd

def get_met_no_12_hour_forecast(latitude, longtitude):
    location = Place("Place", latitude, longtitude)
    forecast = Forecast(location, "My First met.no analyzing app",forecast_type="complete")
    forecast.update()
    forecast_data = forecast.json["data"]["properties"]["timeseries"]
    df_met_no = pd.json_normalize(forecast_data)
    df_met_no['time'] = pd.to_datetime(df_met_no['time']).dt.tz_convert('Europe/Prague')
    df_met_no['time'] = pd.to_datetime(df_met_no['time']).dt.tz_localize(None)
    df_met_no = df_met_no.rename(columns={"time": "DateTime"})
    df_met_no['data.instant.details.wind_speed'] = df_met_no['data.instant.details.wind_speed'] * 3.6
    df_met_no = df_met_no.set_index(['DateTime']).add_prefix('met_no_')
    return df_met_no
