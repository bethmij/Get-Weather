import json
import time
from threading import Thread

import requests


class GetImg(Thread):
    def __init__(self, queries):
        super(GetImg, self).__init__()
        self.queries = queries

    def run(self):
        url = f'https://unsplash.com/napi/search/photos?page=1&query={self.queries}'

        response = requests.get(url)

        if response.status_code == 200:
            resp_json = json.loads(response.content)
            results = resp_json['results']
            print(results)
        else:
            print('Image could\'t be retrieved')

        time.sleep(5)
