import ccxt
import pandas as pd
import numpy as np
import time
import datetime
import loginFTX

exchange = loginFTX.loginx()
def ordercreate(status,amount,price):
    exchange.create_order('XRP-PERP','limit',status,amount,price)
"""
def loginx():
    return (ccxt.ftx({
    'apiKey': 'Your_API',
    'secret': 'Your_secret',
    }))
"""

status = 'buy'
amount = 1
price = 0.198500

ordercreate(status,amount,price)