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

  

# buy_price = requests.get('https://api.binance.com/api/v3/ticker/24hr', {"symbol": "BTCAUD"}).json()
data = json.dumps(requests.get('https://api.binance.com/api/v3/ticker/24hr', {"symbol": "BTCAUD"}).json(), indent=4)
print(data)