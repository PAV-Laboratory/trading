import ccxt
import pandas as pd
import loginFTX as loginFTX

exchange = loginFTX.loginx()
def ordercreate(status,amount,price):
    exchange.create_order('XRP-PERP','limit',status,amount,price)

status = 'buy'
amount = 1
price = 0.198500

ordercreate(status,amount,price)