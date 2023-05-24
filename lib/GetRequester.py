import requests
import json
import ipdb


class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        people_list = []
        people = json.loads(self.get_response_body())
        for person in people:
            people_list.append(person)

        return people_list
