import numpy as np
import pandas as pd


# 1. Calculate daily returns
def calculate_daily_returns(prices):
    return prices.pct_change().dropna()


# 2. Calculate annualised volatility
def calculate_annualised_volatility(returns):
    return returns.std() * np.sqrt(252)


# 3. Calculate cumulative returns
def calculate_cumulative_returns(returns):
    return (1 + returns).cumprod() - 1


# 4. Calculate Sharpe ratio
def calculate_sharpe_ratio(returns, risk_free_rate=0.04):
    daily_rf = (1 + risk_free_rate) ** (1 / 252) - 1
    excess_returns = returns - daily_rf

    return (excess_returns.mean() / returns.std()) * np.sqrt(252)


# 5. Calculate maximum drawdown
def calculate_maximum_drawdown(returns):
    portfolio_value = (1 + returns).cumprod()
    running_peak = portfolio_value.cummax()
    drawdown = (portfolio_value - running_peak) / running_peak

    return drawdown.min()


# 6. Calculate beta
def calculate_beta(portfolio_returns, benchmark_returns):
    covariance = portfolio_returns.cov(benchmark_returns)
    benchmark_variance = benchmark_returns.var()

    return covariance / benchmark_variance


# 7. Calculate rolling volatility
def calculate_rolling_volatility(returns, window=30):
    rolling_volatility = (
        returns.rolling(window=window).std() * np.sqrt(252)
    )

    return rolling_volatility