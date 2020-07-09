import ccxt
import pandas as pd
exchange = ccxt.kucoin()
exchange.apiKey = '5f06d59e3988760006e3efbd'
echange.passphrase = 'tongsang'
exchange.secret = '35f65889-d94b-4f57-b930-bbb3940784bc'

exchange.enableRateLimit = True

print(exchange.fetch_balance ()) #look at how much balance

print(exchange.fetchOrders())
#print(exchange.fetch_ticker('BNB/USD')['last'])

#exhange.create_order('BNB/USD','limit','sell',1,15.7)