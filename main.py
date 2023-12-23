from queue import Queue

from get_img import GetImg
from weather_check import WeatherCheck
from set_wallpaper import SetWallpaper

latitude = 6.053519
longitude = 80.220978
api_key = "f7ea23e4c43dab84aca723334945185d"
queries = Queue()
image = Queue()

if __name__ == "__main__":
    weatherCheck = WeatherCheck(latitude, longitude, api_key, queries)
    weatherCheck.start()

    getImage = GetImg(queries, image)
    getImage.start()

    setWallpaper = SetWallpaper(image)
    setWallpaper.start()

    # for i in range(0, 10):
    #     print(queries)
    #     time.sleep(5)

    weatherCheck.join()
    getImage.join()
