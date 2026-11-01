import pandas as pd

from analysis import (
    calculate_daily_returns,
    calculate_annualised_volatility,
    calculate_cumulative_returns,
    calculate_sharpe_ratio,
    calculate_maximum_drawdown,
    calculate_beta
)

# Sample stock prices
prices = pd.DataFrame({
    "AAPL": [100, 105, 110, 108, 115],
    "MSFT": [200, 210, 205, 215, 220]
})

# Sample benchmark returns
benchmark_returns = pd.Series(
    [0.01, -0.02, 0.03, 0.01],
    name="S&P 500"
)

# 1. Daily returns
daily_returns = calculate_daily_returns(prices)

print("\n1. DAILY RETURNS")
print(daily_returns)

# 2. Annualised volatility
volatility = calculate_annualised_volatility(daily_returns)

print("\n2. ANNUALISED VOLATILITY")
print(volatility)

# 3. Cumulative returns
cumulative_returns = calculate_cumulative_returns(daily_returns)

print("\n3. CUMULATIVE RETURNS")
print(cumulative_returns)

# 4. Sharpe ratio
sharpe = calculate_sharpe_ratio(daily_returns["AAPL"])

print("\n4. SHARPE RATIO")
print(sharpe)

# 5. Maximum drawdown
drawdown = calculate_maximum_drawdown(daily_returns["AAPL"])

print("\n5. MAXIMUM DRAWDOWN")
print(drawdown)

# 6. Beta
beta = calculate_beta(
    daily_returns["AAPL"],
    benchmark_returns
)

print("\n6. BETA")
print(beta)

print("\nALL TESTS COMPLETED!")