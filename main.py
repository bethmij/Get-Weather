import requests
import json


def get_weather():
    latitude = 6.053519
    longitude = 80.220978
    api_key = "f7ea23e4c43dab84aca723334945185d"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        json_response = json.loads(response.content)
        print(json_response["weather"][0])


if __name__ == "__main__":
    get_weather()
