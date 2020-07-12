import ccxt
import pandas as pd

def loginx():
    return (ccxt.ftx({
    'apiKey': 'xiR4FvPEdkPpxWVxYrYYlmJFLpKl7NiSVhEF7IXx',
    'secret': 'FP3-k92SBMEMa-623lMNwoISkwVEqHTBvw6PovbV',
    }))