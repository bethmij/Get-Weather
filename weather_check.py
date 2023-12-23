import requests
import json
from threading import Thread
import time


class WeatherCheck(Thread):

    def __init__(self, latitude, longitude, api_key, queries):
        super(WeatherCheck,self).__init__()
        self.latitude = latitude
        self.longitude = longitude
        self.api_key = api_key
        self.queries = queries
        self.weather = {}

    def run(self):
        while True:
            weather = self.get_weather(self.latitude, self.longitude, self.api_key)
            self.update_weather(weather)
            self.queries.put(self.weather)
            time.sleep(5)

    def update_weather(self, weather):
        for attr in ['id', 'main', 'description', 'icon']:
            self.weather[attr] = weather[attr]

    def get_weather(self, latitude, longitude, api_key):
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            json_response = json.loads(response.content)
            return json_response["weather"][0]
