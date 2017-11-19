import requests
import json
        
def get_price_simple():
    req1 = requests.get("https://www.bitstamp.net/api/v2/ticker/btcusd/")
    btc = json.loads(req1.content.decode("utf-8"))['last']
    return btc

def get_price():
    req1 = requests.get("https://www.bitstamp.net/api/v2/ticker/btcusd/")
    btc = json.loads(req1.content.decode("utf-8"))
    return btc
