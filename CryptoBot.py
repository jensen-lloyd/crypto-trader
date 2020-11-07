#This script is to run our neural network model and execute trades based upon the output of the model

import smtplib
import time
from time import sleep
from datetime import datetime
import requests
import json
import hashlib

# Start Up
print("Crypto trading bot 0.35")
# time = str(datetime.now().time())[:-10]
time = str(datetime.now().time())[:8]

# Email login

secrets = open("secrets.txt", "r")
gmail_username = secrets.readline()
gmail_password = secrets.readline()


def smtp_send(sender, recipient, subject, body='test'):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_username, gmail_password)
    message = '\r\n'.join(['To: %s' % recipient,
                    'From: %s' % sender,
                    'Subject: %s' % subject,
                    '', body])
    server.sendmail(sender, recipient, message)
    print("\nEmail sent successfully!")
    server.quit()

recipient = secrets.readline() # for email notifications and updates


#Test API connection
try:
    price = requests.get('https://api.binance.com/api/v3/ping').json()
    # sell_price = price['prices']['btc']['bid']
    # buy_price = price['prices']['btc']['ask']
    # print('\nBuy price: ' + str(buy_price) + '\nSell price: ' + str(sell_price))
    print("\nAPI connection successful.")

except:
    print("\nAPI connection failed.")

# Send initialiazation email
subject = ('Crypto trading bot is now active.')
body = ('Crypto trading bot is now active.\n\n' + 'Time: ' + time)
# smtp_send(gmail_username, recipient, subject, body)



    
print('')