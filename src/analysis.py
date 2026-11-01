import numpy as np
import pandas as pd


def calculate_daily_returns(prices):
    """Calculate daily percentage returns."""
    return prices.pct_change().dropna()


def calculate_annualised_volatility(returns):
    """Calculate annualised volatility."""
    return returns.std() * np.sqrt(252)


def calculate_cumulative_returns(returns):
    """Calculate cumulative returns."""
    return (1 + returns).cumprod() - 1


def calculate_sharpe_ratio(returns, risk_free_rate=0.04):
    """Calculate annualised Sharpe ratio."""
    daily_rf = (1 + risk_free_rate) ** (1 / 252) - 1
    excess_returns = returns - daily_rf

    return (
        excess_returns.mean() / returns.std()
    ) * np.sqrt(252)


def calculate_maximum_drawdown(returns):
    """Calculate maximum drawdown."""
    portfolio_value = (1 + returns).cumprod()
    running_peak = portfolio_value.cummax()

    drawdown = (
        portfolio_value - running_peak
    ) / running_peak

    return drawdown.min()


def calculate_beta(portfolio_returns, benchmark_returns):
    """Calculate portfolio beta."""
    covariance = portfolio_returns.cov(benchmark_returns)
    benchmark_variance = benchmark_returns.var()

    return covariance / benchmark_variance