import yfinance as yf
import pandas as pd

def get_price_data(tickers, start, end):
    data = yf.download(tickers, start = start, end = end, progress = False, auto_adjust = True)

    data = data.sort_index()
    data = data.ffill().bfill()

    # if isinstance(data.columns, pd.MultiIndex) :
    #     if "Close" in data.columns.get_level_values(0):
    #         prices = data.xs("Close", level = "Price")
    #     else:
    #         raise KeyError("Could not find 'Close' in MultiIndex columns.")
    # else:
    #     if "Close" in data.columns:
    #         prices = data["Close"]
    #     else:
    #         raise KeyError("Could not find 'Close' in columns.")

    if isinstance(data, pd.Series):
        data = data.to_frame()

    return data

def compute_returns(price_df):
    return price_df.pct_change().dropna()


