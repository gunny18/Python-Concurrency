import requests
import time
import threading
from bs4 import BeautifulSoup

class YahooPriceReaderScheduler(threading.Thread):
    COMAPNY_PRICE_DICT = {}
    def __init__(self,inputQ,**kwargs):
        self._inputQ = inputQ
        super(YahooPriceReaderScheduler,self).__init__(**kwargs)
        self.start()
    
    def run(self):
        while True:
            symbol = self._inputQ.get()
            # blocks until we get a value
            if symbol == "DONE":
                break
            y = YahooPriceReader(symbol)
            p = y.get_price()
            YahooPriceReaderScheduler.COMAPNY_PRICE_DICT[symbol] = p




class YahooPriceReader():
    BASE_URL = "https://finance.yahoo.com/quote"
    def __init__(self,symbol):
        self._symbol = symbol

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
                print(f"Price for {self._symbol}---->{price}")
                return price
        except Exception as exc:
            print(f"An error has occured for {self._symbol}---->{exc}")
            return None
        
    def get_price(self):
        return self._getCompanyPrice()



