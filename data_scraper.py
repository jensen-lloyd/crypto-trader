import requests
import json
from datetime import datetime
from time import sleep
import csv


try:
    requests.get('https://api.binance.com/api/v3/ping').json()
except:
    print("Connection failed")


time = str(datetime.now().time())[:5]



def get_data():

    time = str(datetime.now().time())[:5]
    print("\n\nTime: " + time + '\n')

    with open('BTCAUD_data.csv', mode='r') as BTCAUD_data:
        reader = csv.reader(BTCAUD_data, delimiter=',')
        data = list(reader)[-1]

    previous_buy_price = data[5]
    previous_sell_price = data[7]

    print(previous_sell_price)
    print(previous_buy_price)


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


    with open('BTCAUD_data.csv', mode='w') as BTCAUD_data:
        writer = csv.writer(BTCAUD_data, delimiter=',')

        writer.writerow([previous_buy_price, previous_sell_price])
        writer.writerow([raw_price_change, price_change_percent, weighted_avg, last_price, last_qty, bid_price, bid_qty, ask_price, ask_qty, open_price, high_price, low_price, trading_volume, quote_volume])



def main():

    time = str(datetime.now().time())[:5]

    if time == "6:50":
        exit()

    if time[3:] == "0":
        get_data()

    if time[3:] == "15":
        get_data()

    if time[3:] == "30":
        get_data()

    if time[3:] == "45":
        get_data()


    sleep(60)


        
while True:
    main()