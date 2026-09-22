import requests
import openmeteo_requests
from plyer import notification

city = "Jakarta"
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city, "count": 1}
geo_res = requests.get(geo_url, params = geo_params).json()

print(geo_res)

if "results" in geo_res :
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast?latitude=-6.1818&longitude=106.8223&hourly=temperature_2m"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    weather_res = openmeteo_requests.weather_api(weather_url, params=weather_params).json()

    print(weather_res)

    if "curent_weather" in weather_res:
        temp = weather_res["current_weather"]["temperature"]
        wind = weather_res["cureent_weather"]["windspeed"]
        weather_info = f"{city}: {temp} Celcius, Wind {wind} km/h"

        print("Weather:", weather_info)
        notification.notify(
            title = "Weather Update",
            message = weather_info,
            timeout = 5
        )
    else:
        print("Weather data not found")
else:
    print("City not found")