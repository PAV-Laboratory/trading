import ccxt
import pandas as pd



exchange = ccxt.kucoin({
    'apiKey': '5f06d59e3988760006e3efbd',
    'secret': '35f65889-d94b-4f57-b930-bbb3940784bc',
    'password' : 'tongsang'
})

#def ordercreate(status,amount,price):
 #   exchange.create_order('BNB/USDT','limit',status,amount,price)

#print(exchange.fetch_balance ()) #look at how much balance

#print(exchange.fetch_total_balance())
#print(exchange.fetch_ticker('BNB/USD')['last'])

#ordercreate('buy',0.001,16.0)