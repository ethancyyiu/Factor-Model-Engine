import pandas as pd
import numpy as np

def rank_factor(factors):
    return factor.rank(axis = 1, method = "first")

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

    