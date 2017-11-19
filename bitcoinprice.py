import requests
import json
        
url_base = "https://www.bitstamp.net/api/v2/ticker/"

all_pairs = ['btcusd', 'btceur', 'eurusd', 'xrpusd', 'xrpeur', 'xrpbtc', 'ltcusd', 'ltceur', 'ltcbtc', 'ethusd', 'etheur', 'ethbtc']

# Returns dict with last, ask, bid, etc
def get_price_simple(coin='btc', curr='usd'):
    url = url_base + coin + curr + "/"
    result = requests.get(url)
    btc = json.loads(result.content.decode("utf-8"))['last']
    return btc

# Returns string of current price
def get_price(coin='btc', curr='usd'):
    url = url_base + coin + curr + "/"
    result = requests.get(url)
    btc = json.loads(result.content.decode("utf-8"))
    return btc
