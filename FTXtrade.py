import ccxt
import pandas as pd

exchange = ccxt.ftx({
    'apiKey': 'xiR4FvPEdkPpxWVxYrYYlmJFLpKl7NiSVhEF7IXx',
    'secret': 'FP3-k92SBMEMa-623lMNwoISkwVEqHTBvw6PovbV',
})

def ordercreate(status,amount,price):
    exchange.create_order('XRP-PERP','limit',status,amount,price)

status = 'buy'
amount = 1
price = 0.198500

ordercreate(status,amount,price)