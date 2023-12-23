import time

from weather_check import WeatherCheck

latitude = 6.053519
longitude = 80.220978
api_key = "f7ea23e4c43dab84aca723334945185d"
weather = {}

if __name__ == "__main__":
    weatherCheck = WeatherCheck(latitude, longitude, api_key, weather)
    weatherCheck.start()

    for i in range(0, 10):
        print(weather)
        time.sleep(5)
