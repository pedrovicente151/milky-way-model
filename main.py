import requests
from requests import Session
import secrets
from pprint import pprint

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': "078f23d5-6746-4863-b078-3cd159a7a6c5",
}

class CMC:

    def __init__(self, token):
        self.apiurl = "https://pro-api.coinmarketcap.com"
        self.headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token}
        self.session = Session()
        self.session.headers.update(self.headers)

    def get_all_coins(self):
        """Return the top 10 cryptos.
    """
        url = self.apiurl + "/v1/cryptocurrency/listings/latest"
        r = self.session.get(url)
        data = r.json()['data'][:10]
        return data

    def get_names(self):
        url = self.apiurl + "/v1/cryptocurrency/map"
        r = self.session.get(url)
        data = r.json()['data'][:10]

        for i in data:
          if i['id'] == 1:
            pprint(i)

        return data


cmc = CMC("078f23d5-6746-4863-b078-3cd159a7a6c5")
# cmc.get_names()
pprint(cmc.get_all_coins())