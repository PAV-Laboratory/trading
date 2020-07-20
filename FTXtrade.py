import ccxt
import pandas as pd
import numpy as np
import json
import time
import datetime
import loginFTX
import connectgoogle

exchange = loginFTX.loginx()
sheet   =  connectgoogle.opensheet()

def ordercreate(status,amount,price):
    exchange.create_order('XRP-PERP','market',status,amount)

def checkposition():
    return (pd.DataFrame(data=exchange.private_get_positions()))

def checkbalance():
    return (pd.DataFrame(data=exchange.fetch_balance()))

def checkprice():
    return (pd.DataFrame(data=exchange.fetch_tickers('XRP-PERP')))

status = 'buy'
amount = 10
price = 0.198500

position = checkposition() 
price_xrp   =   checkprice()
ask_xrp =   price_xrp.iloc[0]
bid_xrp = price_xrp.iloc[4]
amount_p = position["result"][0]["collateralUsed"] * 100 / ((bid_xrp + ask_xrp)/2)

#order = checkbalance()
#ordercreate(status,amount,price)