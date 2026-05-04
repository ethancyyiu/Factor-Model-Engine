import pandas as pd
import numpy as np
import statsmodels.api as sm

def run_ols(y, x, add_constant=True):
    data = pd.concat([y, x], axis=1).dropna()
    y_clean = data.iloc[:, 0]
    X_clean = data.iloc[:, 1:]

    if add_constant:
        X_clean = sm.add_constant(X_clean)

    model = sm.OLS(y_clean, X_clean)
    results = model.fit()

    return results

def annualize_alpha(alpha_daily, periods_per_year=252):
    return alpha_daily * periods_per_year

def annualize_vol(vol_daily, periods_per_year=252):
    return vol_daily * np.sqrt(periods_per_year)

def summerize_regression(y, x, date = 252):
    result = run_ols(y, x)
    parameter = result.params
    tstats = result.tvalues
    r2 = result.rsquared

    daily_alpha = parameter.iloc[0]
    annualized = annualize_alpha(daily_alpha, date)

    summary = {
        "alpha_daily": daily_alpha,
        "alpha_annual": annualized,
        "alpha_tstat": tstats.iloc[0],
        "r2": r2
    }

    for name, value in parameter.iloc[:1, ].items():
        summary[f"beta_{name}"] = value

    for name, value in tstats.iloc[:1, ].items():
        summary[f"beta_{name}_tstats"] = value


