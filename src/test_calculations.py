import numpy as np
import pandas as pd
from analysis import (
    calculate_daily_returns,
    calculate_annualised_volatility,
    calculate_cumulative_returns,
    calculate_maximum_drawdown,
    calculate_beta,
    calculate_sharpe_ratio

)

def test_daily_returns():
    prices = pd.Series([100, 110, 121])
    result = calculate_daily_returns(prices)
    expected = pd.Series([0.10, 0.10], index=[1, 2])
    pd.testing.assert_series_equal(result, expected)


def test_cumulative_returns():
    returns = pd.Series([0.10, 0.10])
    result = calculate_cumulative_returns(returns)
    expected = pd.Series([0.10, 0.21])
    pd.testing.assert_series_equal(result, expected)


def test_annualised_volatility():
    returns = pd.Series([0.01, 0.02, 0.03, 0.04])
    result = calculate_annualised_volatility(returns)
    expected = returns.std() * np.sqrt(252)
    assert np.isclose(result, expected)


def test_maximum_drawdown():
    returns = pd.Series([0.10, -0.20, 0.10])
    result = calculate_maximum_drawdown(returns)
    assert np.isclose(result, -0.20)


def test_beta():
    portfolio = pd.Series([0.01, 0.02, 0.03, 0.04])
    benchmark = pd.Series([0.01, 0.02, 0.03, 0.04])
    result = calculate_beta(portfolio, benchmark)
    assert np.isclose(result, 1.0)

def test_sharpe_ratio():
    returns = pd.Series([0.01, 0.02, 0.03, 0.04])

    result = calculate_sharpe_ratio(returns)

    daily_rf = (1 + 0.04) ** (1 / 252) - 1
    expected = (
        (returns - daily_rf).mean() / returns.std()
    ) * np.sqrt(252)

    assert np.isclose(result, expected)

    