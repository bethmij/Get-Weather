from weatherCheck import WeatherCheck

latitude = 6.053519
longitude = 80.220978
api_key = "f7ea23e4c43dab84aca723334945185d"

if __name__ == "__main__":
    weatherCheck = WeatherCheck()
    weatherCheck.get_weather(latitude, longitude, api_key)
