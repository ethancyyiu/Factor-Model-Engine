import yfinance as yf
import pandas as pd

def get_price_data(tickers, start, end):
    data = yf.download(tickers, start = start, end = end, progress = False, auto_adjust = True)["close"]

    data = data.sort_index()
    data = data.ffill().bfill()

    return data




