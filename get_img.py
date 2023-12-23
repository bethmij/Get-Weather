import json
from multiprocessing import Process
from threading import Thread

import requests


class GetImg(Thread):
    def __init__(self, queries):
        super(GetImg, self).__init__()
        self.queries = queries
        self.previous_query = None

    def run(self):
        queries = self.queries.get()
        self.previous_query = queries
        print("Query :", queries)
        while queries is not None:
            if self.previous_query == queries:
                queries = self.queries.get()
                print("Same Query")
                continue

            url = f'https://unsplash.com/napi/search/photos?page=1&query={queries}'

            response = requests.get(url)

            if response.status_code == 200:
                resp_json = json.loads(response.content)
                results = resp_json['results']
                if len(results) > 0:
                    self.__download_img(results[0])

            else:
                print('Image could\'t be retrieved')

            queries = self.queries.get()
            self.previous_query = queries

    def __download_img(self, results):
        row_img = results['urls']['raw']
        print(row_img)
