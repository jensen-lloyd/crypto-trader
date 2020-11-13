import requests
import json
from datetime import datetime

try:
    requests.get('https://api.binance.com/api/v3/ping').json()
except:
    print("Connection failed")

time = str(datetime.now().time())[:5]





# while time != 6:58:
#     time = str(datetime.now().time())[:5]

  
data = requests.get('https://api.binance.com/api/v3/ticker/24hr', {"symbol": "BTCAUD"}).json()

raw_price_change = data["priceChange"]
print(raw_price_change)

price_change_percent = data["priceChangePercent"]
print(price_change_percent)

weighted_avg = data["weightedAvgPrice"]
print(weighted_avg)

last_price = data["lastPrice"]
print(last_price)

last_qty = data["lastQty"]
print(last_qty)

bid_price = data["bidPrice"]
print(bid_price)

bid_qty = data["bidQty"]
print(bid_qty)

ask_price = data["askPrice"]
print(last_price)

ask_qty = data["askQty"]
print(ask_qty)

open_price = data["openPrice"]
print(open_price)

high_price = data["highPrice"]
print(high_price)

low_price = data["lowPrice"]
print(low_price)

trading_volume = data["volume"]
print(trading_volume)

quote_volume = data["quoteVolume"]
print(quote_volume)



# previous_buy = 
# print(previous_buy)
# previous_sell =
# print(previous_sell) 