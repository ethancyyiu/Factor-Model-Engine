import pandas as pd
import numpy as np
import statsmodels.api as sm

def run_ols(y, X, add_constant=True):
    data = pd.concat([y, X], axis=1).dropna()
    y_clean = data.iloc[:, 0]
    X_clean = data.iloc[:, 1:]

    if add_constant:
        X_clean = sm.add_constant(X_clean)

    model = sm.OLS(y_clean, X_clean)
    results = model.fit()

    return results
