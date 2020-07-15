import ccxt
import pandas as pd
import numpy as np
import time
import datetime
import loginFTX
import connectgoogle

exchange = loginFTX.loginx()
sheet   =  connectgoogle.opensheet()

def ordercreate(status,amount,price):
    exchange.create_order('XRP-PERP','limit',status,amount,price)

status = 'buy'
amount = 1
price = 0.198500

#ordercreate(status,amount,price)