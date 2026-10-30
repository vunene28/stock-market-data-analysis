
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
