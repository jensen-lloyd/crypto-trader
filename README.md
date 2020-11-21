Crypto trader is a project to create a neural network model from scratch in Python (ANN_trainer.py), 
trained on data collected by a Python script (data_scraper.py), 
and another program (CryptoBot.py) to make trading decisions based upon output from the 
Neural Network and then execute the trades via the Binance API.


Usage:
This project is still a work in progress, but "data_scraper.py" is completed and working. 
I am regularly working on it and it should be finished soon!


To use "data_scraper.py" (to get data from Binance API to train our Neural Network on) 
simply edit the "symbol" variable (line 16) to whatever trading pair you have decided to use, personally, I am using "BTCAUD".

I have written in an automatic close at "6:50" AM, this is because I wish to reboot my machine then, if you do not wish for the program to close daily,
then remove these 2 lines


if time == "6:50": 

    exit()
  
  
in lines 116 & 117. You could also change the time if you wish.
