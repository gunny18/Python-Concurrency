import requests
import time
import threading
from bs4 import BeautifulSoup

class YahooPriceReader(threading.Thread):
    BASE_URL = "https://finance.yahoo.com/quote"
    COMPANY_PRICE = {}
    def __init__(self,symbol,**kwargs):
        self._symbol = symbol
        # self.companyPrice = {}
        super(YahooPriceReader,self).__init__(**kwargs)
        self.start()

    def _getResponseObject(self):
        try:
            resp = requests.get(f"{YahooPriceReader.BASE_URL}/{self._symbol}")
            return resp
        except Exception as exc:
            print(f"An error occured for {self._symbol}----->{exc}")
    
    def _getCompanyPrice(self):
        resp = self._getResponseObject()
        try:
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.content, "lxml")
                price = float(soup.find("fin-streamer",
                            attrs={"data-symbol": self._symbol}).get_text().strip().replace(",",""))
                YahooPriceReader.COMPANY_PRICE[self._symbol] = price
                print(f"Price for {self._symbol}---->{price}")
        except Exception as exc:
            print(f"An error has occured for {self._symbol}---->{exc}")
        
    def run(self):
        self._getCompanyPrice()



