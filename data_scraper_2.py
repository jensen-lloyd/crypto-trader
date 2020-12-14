import requests
import json
from datetime import datetime
from time import sleep
import csv


requests.get('https://api.binance.com/api/v3/ping').json()

time = str(datetime.now().time())[:5]

symbol = "BTCAUD"



def main():

    time = str(datetime.now().time())[:5]


    data = requests.get('https://api.binance.com/api/v3/klines', {"symbol": symbol}).json()

    raw_price_change = data["priceChange"]
    price_change_percent = data["priceChangePercent"]
    weighted_avg = data["weightedAvgPrice"]


    with open('BTCAUD_klines_data.csv', mode='a', newline='') as BTCAUD_data:
        writer = csv.writer(BTCAUD_data)

        writer.writerow(['***********'])



while True:
    main()