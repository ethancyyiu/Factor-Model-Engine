import pandas as pd
import numpy as np
from load_data import compute_returns

def momentum_factor(prices):
    momentum = prices.pct_change(252) - prices.pct_change(21)
    return momentum

def volatility_factor(prices, window=21):
    returns = prices.pct_change()
    vol = returns.rolling(window).std()
    return vol


