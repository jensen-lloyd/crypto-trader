Crypto trader is a project to create a neural network model from scratch in Python (ANN_trainer.py), 
trained on data collected by a Python script (data_scraper.py), 
and another program (CryptoBot.py) to make trading decisions based upon output from the 
Neural Network and then execute the trades via the Binance API.


This project is still a work in progress, but "data_scraper.py" is completed and working. 
I am regularly working on it and it should be finished soon!


Full details on how everything is going to work overall is in "plan.txt"


data_scraper.py usage: (to get data from Binance API to train our Neural Network on) 

simply edit the "symbol" variable (line 16) to whatever trading pair you have decided to use, personally, I am using "BTCAUD".
