from cryptocmd import CmcScraper
from pprint import pprint
scraper = CmcScraper('BTC', '24-06-2022', '25-06-2022')
btc_json_data = scraper.get_data('json')
scraper.export('csv',name="btc")

print('Bitcoin: ')
pprint(btc_json_data)
scraper = CmcScraper('ETH', '24-06-2022', '25-06-2022')
eth_json_data = scraper.get_data('json')
print("Ethereum: ")
pprint(eth_json_data)
scraper.export("csv",name='eth')
scraper = CmcScraper('DOGE', '24-06-2022', '25-06-2022')
doge_json_data = scraper.get_data('json')
scraper.export("csv",name='doge')
print("DogeCoin: ")
pprint(doge_json_data)
