import pandas as pd
import numpy as np
from factors import zscore

def rank_factor(factors):
    return factors.rank(axis = 1, method = "first")

def long_short_weights(ranks, long_pct=0.2, short_pct=0.2):
    n_stocks = ranks.shape[1]
    long_cutoff = (1 - long_pct) * n_stocks
    short_cutoff = short_pct * n_stocks

    weights = pd.DataFrame(0.0, index=ranks.index, columns=ranks.columns)
    weights[ranks > long_cutoff] = 1.0
    weights[ranks <= short_cutoff] = -1.0

    return weights

def normalize(weights):
    abs_sum = weights.abs().sum(axis=1)
    abs_sum[abs_sum == 0] = np.nan
    normed = weights.div(abs_sum, axis=0)
    return normed.fillna(0.0)

def portfolio_returns(weights, returns):
    returns = returns.reindex_like(weights)
    port = (weights * returns).sum(axis=1)
    return port

def zscore_weights(factors):
    z = zscore(factors)
    z = z.clip(-3, 3)
    return normalize(z)

def zscore_all_factors(factors_dict):
    return {name: zscore(df) for name, df in factors_dict.items()}

def composite_factor(factors_dict):
    z_factors = zscore_all_factors(factors_dict)
    z_list = list(z_factors.values())
    combined = sum(z_list) / len(z_list)
    return combined


def build_long_short_portfolio(factor_df, returns, long_pct=0.2, short_pct=0.2):
    ranks = rank_factor(factor_df)
    raw_weights = long_short_weights(ranks, long_pct, short_pct)
    weights = normalize(raw_weights)
    port_ret = portfolio_returns(weights, returns)
    return weights, port_ret

def build_zscore_portfolio_from_factor(factor, returns):
    weights = zscore_weights(factor)
    port_ret = portfolio_returns(weights, returns)
    return weights, port_ret

def build_composite_portfolio(factors_dict, returns):
    composite = composite_factor(factors_dict)
    weights = zscore_weights(composite)
    port_ret = portfolio_returns(weights, returns)
    return weights, port_ret




