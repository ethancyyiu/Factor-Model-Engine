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

def reversal_factor(prices):
    rev = -prices.pct_change(5)
    return rev

def sma_distance_factor(prices, window = 20):
    sma = prices.rolling(window).mean()
    dist = prices / sma - 1
    return dist

def compute_all(prices):
    factors = {
        "momentum" = momentum_factor(prices)
        "volatility" = volatility_factor(prices)
        "reversal" = reversal_factor(prices)
        "sma_distance" = sma_distance_factor(prices)
    }
    return factors




