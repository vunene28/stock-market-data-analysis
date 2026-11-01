
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ==========================================
# 1. STOCKS AND HISTORICAL PERIOD
# ==========================================

tickers = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "^GSPC"]

start_date = "2021-01-01"
end_date = "2026-01-01"


# ==========================================
# 2. DOWNLOAD STOCK MARKET DATA
# ==========================================

stock_data = yf.download(
    tickers,
    start=start_date,
    end=end_date,
    auto_adjust=True,
    progress=False
)

# Extract adjusted closing prices
closing_prices = stock_data["Close"]

# Save stock prices
closing_prices.to_csv("data/stock_prices.csv")

print("Data successfully saved!")
print(closing_prices.head())


# ==========================================
# 3. INSPECT THE DATASET
# ==========================================

print("\nDataset information:")
print(closing_prices.info())

print("\nDataset shape:")
print(closing_prices.shape)

print("\nMissing values:")
print(closing_prices.isnull().sum())

print("\nSummary statistics:")
print(closing_prices.describe())


# ==========================================
# 4. CALCULATE DAILY RETURNS
# ==========================================

daily_returns = closing_prices.pct_change()

# Remove first row because it has no previous trading day
daily_returns = daily_returns.dropna()

# Save daily returns
daily_returns.to_csv("data/daily_returns.csv")

print("\nDaily returns:")
print(daily_returns.head())


# ==========================================
# 5. CALCULATE ANNUALISED VOLATILITY
# ==========================================

daily_volatility = daily_returns.std()

annual_volatility = daily_volatility * (252 ** 0.5)

# Convert to percentages
annual_volatility_percentage = annual_volatility * 100

print("\nAnnualised Volatility:")
print(annual_volatility_percentage.sort_values(ascending=False))


# ==========================================
# 6. PLOT ANNUALISED VOLATILITY
# ==========================================

annual_volatility_percentage.sort_values().plot(
    kind="bar",
    figsize=(10, 6),
    title="Annualised Volatility (2021–2025)"
)

plt.ylabel("Annualised Volatility (%)")
plt.xlabel("Stock / Index")
plt.tight_layout()

plt.savefig("figures/annualised_volatility.png")

plt.show()


# ==========================================
# 7. CALCULATE CUMULATIVE RETURNS
# ==========================================

cumulative_returns = (1 + daily_returns).cumprod() - 1

# Save cumulative returns
cumulative_returns.to_csv("data/cumulative_returns.csv")

print("\nCumulative Returns:")
print(cumulative_returns.tail())


# ==========================================
# 8. PLOT CUMULATIVE RETURNS
# ==========================================

cumulative_returns.plot(
    figsize=(12, 6),
    title="Cumulative Returns (2021–2025)"
)

plt.ylabel("Cumulative Return")
plt.xlabel("Date")
plt.legend(title="Stock / Index")
plt.tight_layout()

plt.savefig("figures/cumulative_returns.png")

plt.show()


# ==========================================
# 9. CALCULATE CORRELATION MATRIX
# ==========================================

correlation_matrix = daily_returns.corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

# Save correlation matrix
correlation_matrix.to_csv("data/correlation_matrix.csv")


# ==========================================
# 10. PLOT CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(10, 8))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Stock Returns Correlation Matrix (2021–2025)")
plt.tight_layout()

plt.savefig("figures/correlation_heatmap.png")

plt.show()

print("\nStock market analysis completed successfully!")

# ==========================================
# 11. CONSTRUCT AN EQUAL-WEIGHTED PORTFOLIO
# ==========================================

# Select the five individual stocks
portfolio_stocks = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL"]

# Assign equal weights to each stock
weights = [0.20, 0.20, 0.20, 0.20, 0.20]

# Calculate daily portfolio returns
portfolio_returns = (
    daily_returns[portfolio_stocks] * weights
).sum(axis=1)

# Save portfolio returns
portfolio_returns.to_csv("data/portfolio_returns.csv")

print("\nEqual-Weighted Portfolio Daily Returns:")
print(portfolio_returns.head())


# ==========================================
# 12. CALCULATE PORTFOLIO RISK
# ==========================================

# Calculate daily portfolio volatility
portfolio_daily_volatility = portfolio_returns.std()

# Annualise portfolio volatility
portfolio_annual_volatility = portfolio_daily_volatility * (252 ** 0.5)

print("\nPortfolio Annualised Volatility:")
print(f"{portfolio_annual_volatility * 100:.2f}%")


# ==========================================
# 13. CALCULATE PORTFOLIO CUMULATIVE RETURN
# ==========================================

portfolio_cumulative_returns = (
    (1 + portfolio_returns).cumprod() - 1
)

print("\nPortfolio Cumulative Return:")
print(f"{portfolio_cumulative_returns.iloc[-1] * 100:.2f}%")


# ==========================================
# 14. COMPARE PORTFOLIO WITH S&P 500
# ==========================================

benchmark_returns = daily_returns["^GSPC"]

benchmark_cumulative_returns = (
    (1 + benchmark_returns).cumprod() - 1
)

comparison = pd.DataFrame({
    "Equal-Weighted Portfolio": portfolio_cumulative_returns,
    "S&P 500": benchmark_cumulative_returns
})

comparison.to_csv("data/portfolio_vs_benchmark.csv")

# Plot comparison
comparison.plot(
    figsize=(12, 6),
    title="Equal-Weighted Portfolio vs S&P 500 (2021–2025)"
)

plt.ylabel("Cumulative Return")
plt.xlabel("Date")
plt.legend(title="Investment")
plt.tight_layout()

plt.savefig("figures/portfolio_vs_benchmark.png")

plt.show()

print("\nPortfolio analysis completed successfully!")
# ==========================================
# 15. CALCULATE SHARPE RATIO
# ==========================================

# Assume a risk-free rate of 4% per annum
risk_free_rate = 0.04

# Convert annual risk-free rate to daily rate
daily_risk_free_rate = (
    (1 + risk_free_rate) ** (1 / 252)
) - 1

# Calculate daily excess returns
excess_returns = (
    portfolio_returns - daily_risk_free_rate
)

# Calculate annualised Sharpe ratio
sharpe_ratio = (
    excess_returns.mean() / portfolio_returns.std()
) * (252 ** 0.5)

print("\nPortfolio Sharpe Ratio:")
print(f"{sharpe_ratio:.4f}")

# ==========================================
# 16. CALCULATE MAXIMUM DRAWDOWN
# ==========================================

# Calculate portfolio value over time
portfolio_value = (1 + portfolio_returns).cumprod()

# Calculate the running maximum
running_peak = portfolio_value.cummax()

# Calculate drawdown
drawdown = (portfolio_value - running_peak) / running_peak

# Calculate maximum drawdown
maximum_drawdown = drawdown.min()

print("\nPortfolio Maximum Drawdown:")
print(f"{maximum_drawdown * 100:.2f}%")

# ==========================================
# 17. PORTFOLIO PERFORMANCE SUMMARY
# ==========================================

performance_summary = pd.DataFrame({
    "Metric": [
        "Cumulative Return",
        "Annualised Volatility",
        "Sharpe Ratio",
        "Maximum Drawdown"
    ],
    "Value": [
        f"{portfolio_cumulative_returns.iloc[-1] * 100:.2f}%",
        f"{portfolio_annual_volatility * 100:.2f}%",
        f"{sharpe_ratio:.4f}",
        f"{maximum_drawdown * 100:.2f}%"
    ]
})

print("\nPORTFOLIO PERFORMANCE SUMMARY")
print(performance_summary)

# Save summary
performance_summary.to_csv(
    "data/portfolio_performance_summary.csv",
    index=False
)

# ==========================================
# 18. S&P 500 BENCHMARK PERFORMANCE METRICS
# ==========================================

# Calculate benchmark cumulative return
benchmark_cumulative_return = benchmark_cumulative_returns.iloc[-1]

# Calculate benchmark annualised volatility
benchmark_annual_volatility = (
    benchmark_returns.std() * (252 ** 0.5)
)

# Calculate benchmark Sharpe ratio
benchmark_excess_returns = (
    benchmark_returns - daily_risk_free_rate
)

benchmark_sharpe_ratio = (
    benchmark_excess_returns.mean()
    / benchmark_returns.std()
) * (252 ** 0.5)

# Calculate benchmark maximum drawdown
benchmark_value = (1 + benchmark_returns).cumprod()

benchmark_running_peak = benchmark_value.cummax()

benchmark_drawdown = (
    benchmark_value - benchmark_running_peak
) / benchmark_running_peak

benchmark_max_drawdown = benchmark_drawdown.min()

# Display benchmark metrics
print("\nS&P 500 BENCHMARK PERFORMANCE")

print(f"Cumulative Return: {benchmark_cumulative_return * 100:.2f}%")
print(f"Annualised Volatility: {benchmark_annual_volatility * 100:.2f}%")
print(f"Sharpe Ratio: {benchmark_sharpe_ratio:.4f}")
print(f"Maximum Drawdown: {benchmark_max_drawdown * 100:.2f}%")
# ==========================================
# 19. PORTFOLIO VS BENCHMARK COMPARISON
# ==========================================

comparison_summary = pd.DataFrame({
    "Metric": [
        "Cumulative Return",
        "Annualised Volatility",
        "Sharpe Ratio",
        "Maximum Drawdown"
    ],
    "Equal-Weighted Portfolio": [
        f"{portfolio_cumulative_returns.iloc[-1] * 100:.2f}%",
        f"{portfolio_annual_volatility * 100:.2f}%",
        f"{sharpe_ratio:.4f}",
        f"{maximum_drawdown * 100:.2f}%"
    ],
    "S&P 500": [
        f"{benchmark_cumulative_return * 100:.2f}%",
        f"{benchmark_annual_volatility * 100:.2f}%",
        f"{benchmark_sharpe_ratio:.4f}",
        f"{benchmark_max_drawdown * 100:.2f}%"
    ]
})

print("\nPORTFOLIO VS S&P 500 COMPARISON")
print(comparison_summary)

comparison_summary.to_csv(
    "data/portfolio_vs_benchmark_summary.csv",
    index=False
)# ==========================================
# 20. PORTFOLIO BETA AND ALPHA
# ==========================================

# Calculate covariance between portfolio and benchmark
covariance = portfolio_returns.cov(benchmark_returns)

# Calculate benchmark variance
benchmark_variance = benchmark_returns.var()

# Calculate portfolio beta
portfolio_beta = covariance / benchmark_variance

# Calculate annualised portfolio and benchmark returns
portfolio_annual_return = portfolio_returns.mean() * 252
benchmark_annual_return = benchmark_returns.mean() * 252

# Calculate annualised alpha using CAPM
portfolio_alpha = (
    portfolio_annual_return
    - (
        risk_free_rate
        + portfolio_beta * (benchmark_annual_return - risk_free_rate)
    )
)

print("\nPORTFOLIO BETA AND ALPHA")
print(f"Portfolio Beta: {portfolio_beta:.4f}")
print(f"Portfolio Alpha: {portfolio_alpha * 100:.2f}%")

# ==========================================
# 21. RISK-RETURN COMPARISON
# ==========================================

# Calculate annualised returns
portfolio_annual_return = portfolio_returns.mean() * 252
benchmark_annual_return = benchmark_returns.mean() * 252

# Create comparison dataset
risk_return = pd.DataFrame({
    "Asset": ["Equal-Weighted Portfolio", "S&P 500"],
    "Annualised Risk": [
        portfolio_annual_volatility * 100,
        benchmark_annual_volatility * 100
    ],
    "Annualised Return": [
        portfolio_annual_return * 100,
        benchmark_annual_return * 100
    ]
})

# Plot risk-return relationship
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=risk_return,
    x="Annualised Risk",
    y="Annualised Return",
    hue="Asset",
    s=200
)

plt.title("Risk-Return Comparison")
plt.xlabel("Annualised Volatility (%)")
plt.ylabel("Annualised Return (%)")
plt.grid(True)

plt.savefig("figures/risk_return_comparison.png")
plt.show()

print("\nRisk-return comparison saved successfully!")

# ==========================================
# 22. FINAL PERFORMANCE REPORT
# ==========================================

final_report = pd.DataFrame({
    "Metric": [
        "Cumulative Return",
        "Annualised Volatility",
        "Sharpe Ratio",
        "Maximum Drawdown",
        "Annualised Return",
        "Beta",
        "Alpha"
    ],
    "Portfolio": [
        f"{portfolio_cumulative_returns.iloc[-1] * 100:.2f}%",
        f"{portfolio_annual_volatility * 100:.2f}%",
        f"{sharpe_ratio:.4f}",
        f"{maximum_drawdown * 100:.2f}%",
        f"{portfolio_annual_return * 100:.2f}%",
        f"{portfolio_beta:.4f}",
        f"{portfolio_alpha * 100:.2f}%"
    ],
    "S&P 500": [
        f"{benchmark_cumulative_return * 100:.2f}%",
        f"{benchmark_annual_volatility * 100:.2f}%",
        f"{benchmark_sharpe_ratio:.4f}",
        f"{benchmark_max_drawdown * 100:.2f}%",
        f"{benchmark_annual_return * 100:.2f}%",
        "N/A",
        "N/A"
    ]
})

print("\nFINAL PERFORMANCE REPORT")
print(final_report)

final_report.to_csv(
    "data/final_performance_report.csv",
    index=False
)

print("\nFinal performance report saved successfully!")
# ==========================================
# 23. DATA VALIDATION
# ==========================================

print("\nDATA VALIDATION REPORT")

# Check for missing values
print("\nMissing values:")
print(closing_prices.isnull().sum())

# Check for duplicate dates
print("\nDuplicate dates:")
print(closing_prices.index.duplicated().sum())

# Check for infinite values in returns
print("\nInfinite values in daily returns:")
print(np.isinf(daily_returns).sum())

# Check portfolio weights
print("\nPortfolio weights:")
print(f"Total weight: {sum(weights):.2f}")

# Validate portfolio weights
assert abs(sum(weights) - 1.0) < 1e-10, "Portfolio weights must sum to 1."

# Check whether returns contain missing values
assert not daily_returns.isnull().any().any(), "Missing returns detected."

print("\nData validation completed!")