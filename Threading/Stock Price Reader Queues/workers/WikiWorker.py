import threading
from bs4 import BeautifulSoup
import requests


class WikiWorker(threading.Thread):
    def __init__(self, url, **kwargs):
        self._url = url
        self.companies = None
        super(WikiWorker, self).__init__(**kwargs)
        self.start()

    def _getResponseObject(self):
        resp = requests.get(self._url)
        return resp

    def _getCompanies(self):
        resp = self._getResponseObject()
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "lxml")
            self.companies = [a.text for a in soup.findAll(
                "a", attrs={"rel": "nofollow", "class": "external text"}) if len(a.text) <= 6]

    def run(self):
        self._getCompanies()
