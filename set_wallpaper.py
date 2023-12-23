import os
import time
from os import path
from threading import Thread
import ctypes
SPI_SETDESKWALLPAPER = 20


class SetWallpaper(Thread):
    def __init__(self, image):
        super(SetWallpaper, self).__init__()
        self.image = image

    def run(self):
        image = self.image.get()
        while True:
            file_name = image.split('/')[-1]
            image = path.join(os.getcwd(), 'image', file_name)
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, 0)
            time.sleep(5)
            image = self.image.get()
