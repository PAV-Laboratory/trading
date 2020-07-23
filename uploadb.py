import ccxt
import pandas as pd
import numpy as np
import math
import json
import time
import datetime
import loginFTXb
#import connectgoogle

exchange = loginFTXb.loginx()
exchange.headers = {'FTX-SUBACCOUNT':'BuySide'}
#sheet   =  connectgoogle.opensheet()

def ordercreate(status,amount):
    exchange.create_order('XRP-PERP','market',status,amount)
    #if(last_price - avg_price > 0)
    return 0

def checkposition():
    return (pd.DataFrame(data=exchange.private_get_positions()))

def checkbalance():
    return (pd.DataFrame(data=exchange.fetch_balance()))

def checkprice():
    return (pd.DataFrame(data=exchange.fetch_tickers('XRP-PERP')))

def calamount(start_price,start_amount,avg_price,step):
    if((start_price - avg_price)<0):
        return (start_amount-(round_down(abs(np.subtract(start_price,avg_price)),3)) * (step))
    else:
        return (start_amount+(round_up(abs(np.subtract(start_price,avg_price)),3)) * (step))
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
def checkamount(position,avg_price):
    return position["result"][0]["netSize"]
def ordering(amount_p,amount_want):
	if(amount_p > amount_want):
        #print ('Sell %f'%(abs(amount_p-amount_want)))
		ordercreate('sell',abs(amount_p-amount_want))
	elif(amount_p < amount_want):
        #print ('Buy %f'%(abs(amount_p-amount_want)))
		ordercreate('buy',abs(amount_p-amount_want))
    #else:
        #print('none')
position = checkposition() 
price_xrp   =   checkprice()
ask_xrp =   price_xrp.iloc[0]
bid_xrp = price_xrp.iloc[4]
avg_price = (bid_xrp[0] + ask_xrp[0])/2
start_price = 0.19687
start_amount = 1000
step = 60000
amount_p = abs(checkamount(position,avg_price))
amount_want = abs(calamount(start_price,start_amount,avg_price,step))

if(avg_price < 0.211 and avg_price > 0.18  ):
    ordering(amount_p,amount_want)
else:
    if(amount_p!=0):
        ordercreate('sell',amount_p)
        



#order = checkbalance()
#ordercreate(status,amount,price)
