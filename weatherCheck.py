import requests
import json


class WeatherCheck:
    def get_weather(self, latitude, longitude, api_key):
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            json_response = json.loads(response.content)
            print(json_response["weather"][0])
