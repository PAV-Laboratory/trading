import ccxt
import pandas as pd

def loginx():
    return (ccxt.ftx({
    'FTX-SUBACCOUNT':'BuySide',
    'apiKey': '197k2kYpGvyHMy__2H0WGVoHU_TPNkuydWtiig0h',
    'secret': 'toncOlJhZfKO48jb6WLUJ59G67Z6-2EP2uVWCeWh',
    }))
