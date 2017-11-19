import bitcoinprice 
from pprint import pprint

pprint(bitcoinprice.get_price())
pprint(bitcoinprice.get_price('btc', 'eur'))
pprint(bitcoinprice.get_price('ltc', 'eur'))

pprint("Price Simple (usd):"+bitcoinprice.get_price_simple())
pprint("Price Simple (eur):"+bitcoinprice.get_price_simple('btc','eur'))
pprint("Price Simple (eth):"+bitcoinprice.get_price_simple('eth'))
pprint("Price Simple (ltc):"+bitcoinprice.get_price_simple('ltc'))
