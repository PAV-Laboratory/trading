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
    exchange.create_order('XRP-PERP','limit',status,amount,price)

def checkposition():
    return (pd.DataFrame(data=exchange.private_get_positions()))

def checkbalance():
    return (pd.DataFrame(data=exchange.fetch_balance()))

status = 'buy'
amount = 1
price = 0.198500

history = checkposirtion()
order = checkbalance()
#ordercreate(status,amount,price)