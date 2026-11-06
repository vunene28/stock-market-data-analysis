# Stock Market Data Analysis

## Overview

This project analyses historical stock market data using Python. It examines the performance and risk of five major technology companies and compares an equally weighted portfolio against the S&P 500 benchmark.

The analysis covers the period from January 2021 to December 2025.

## Project Objectives

- Collect historical stock market data.
- Calculate daily stock returns.
- Measure investment risk and performance.
- Analyse portfolio performance against the S&P 500.
- Calculate financial risk metrics.
- Visualise market trends and portfolio performance.
- Apply Python testing to verify calculations.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- yfinance
- Pytest

## Stocks Analysed

The project examines the following companies:

- Apple (AAPL)
- Microsoft (MSFT)
- NVIDIA (NVDA)
- Amazon (AMZN)
- Alphabet (GOOGL)

The S&P 500 (^GSPC) is used as the benchmark.

## Financial Metrics

The project calculates:

- Daily Returns
- Cumulative Returns
- Annualised Volatility
- Sharpe Ratio
- Maximum Drawdown
- Beta
- Alpha
- Rolling Volatility
- Correlation Matrix

The portfolio is equally weighted, with each of the five stocks receiving a 20% allocation.

## Key Results

The analysis produced the following portfolio results:

| Metric | Portfolio | S&P 500 |
|---|---:|---:|
| Cumulative Return | 268.40% | 84.98% |
| Annualised Volatility | 28.22% | 16.96% |
| Sharpe Ratio | 0.9307 | 0.5824 |
| Maximum Drawdown | -41.83% | -25.43% |
| Annualised Return | 30.19% | 13.80% |

The portfolio achieved a higher cumulative return than the benchmark over the selected period, while also experiencing higher volatility and a larger maximum drawdown.

These results are historical and do not guarantee future performance.

## Project Structure

```text
stock-market-data-analysis/
│
├── data/
│   ├── correlation_matrix.csv
│   ├── cumulative_returns.csv
│   ├── daily_returns.csv
│   ├── final_performance_report.csv
│   ├── portfolio_performance_summary.csv
│   ├── portfolio_returns.csv
│   ├── portfolio_rolling_volatility.csv
│   ├── portfolio_vs_benchmark.csv
│   ├── portfolio_vs_benchmark_summary.csv
│   └── stock_prices.csv
│
├── figures/
│   ├── annualised_volatility.png
│   ├── correlation_heatmap.png
│   ├── cumulative_returns.png
│   ├── portfolio_vs_benchmark.png
│   ├── risk_return_comparison.png
│   └── rolling_volatility.png
│
├── notebooks/
│
├── src/
│   ├── analysis.py
│   ├── download_data.py
│   ├── test_analysis.py
│   └── test_calculations.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/vunene28/stock-market-data-analysis.git
```

### 2. Navigate into the project

```bash
cd stock-market-data-analysis
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download and analyse the data

```bash
python src/download_data.py
```

### 5. Run the tests

```bash
python -m pytest -v
```

## Testing

The project includes automated tests using Pytest to verify the financial calculation functions.

Latest test result: **7 tests passed.**

## Author

**Vunene Mahambane**

BSc Mathematical and Computer Sciences Student

Interested in quantitative finance, financial engineering, and data analysis.