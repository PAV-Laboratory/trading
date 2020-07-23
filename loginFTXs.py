import ccxt
import pandas as pd

def loginx():
    return (ccxt.ftx({
    'FTX-SUBACCOUNT':'SellSide',
    'apiKey': '5EsdFqBumKhLnX6BLAXcWSWj54EuquB0QpCIu6ZE',
    'secret': 'iCWYk3XiJetOAz3WehDdaPXbPxdTj5w2kk9zZ7pK',
    }))
