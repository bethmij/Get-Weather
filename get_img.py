import json
from multiprocessing import Process
from threading import Thread

import requests


class GetImg(Thread):
    def __init__(self, queries, image):
        super(GetImg, self).__init__()
        self.queries = queries
        self.previous_query = None
        self.image = image

    def run(self):
        queries = self.queries.get()
        # self.previous_query = queries
        print("Query :", queries)
        while queries is not None:
            if self.previous_query == queries:
                queries = self.queries.get()
                print("Same Query")
                continue

            dsp = queries['description']
            url = f'https://unsplash.com/napi/search/photos?page=1&query={dsp}'

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
        response = requests.get(row_img, stream=True)

        if response.status_code == 200:
            response.raw.decode_content = True
            x = row_img.split('?')
            image_name = x[0].split('/')[-1]

            path = f"image/{image_name}.jpg"
            if response.status_code == 200:
                with open(path, "wb") as f:
                    f.write(response.content)
                print("Image downloaded successfully.")
                self.image.put(path)
                return True
            else:
                print(f"Failed to download image. Status code: {response.status_code}")
                return False
