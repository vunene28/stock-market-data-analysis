# Stock Market Data Analysis

## Overview

This project analyses historical stock market data using Python to evaluate the performance and risk characteristics of an equally weighted portfolio of selected technology companies against the S&P 500 benchmark.

The project applies quantitative finance concepts, statistical analysis and data visualisation to explore investment performance, portfolio risk and market exposure.

## Objectives

* Retrieve and analyse historical stock market data.
* Calculate daily and cumulative returns.
* Construct an equally weighted investment portfolio.
* Measure portfolio risk and performance.
* Compare portfolio performance against the S&P 500.
* Calculate financial risk metrics.
* Visualise financial data and communicate analytical findings.

## Assets Analysed

| Company   | Ticker |
| --------- | ------ |
| Apple     | AAPL   |
| Microsoft | MSFT   |
| NVIDIA    | NVDA   |
| Amazon    | AMZN   |
| Alphabet  | GOOGL  |

**Benchmark:** S&P 500 (`^GSPC`)

**Data period:** January 2021 – December 2025.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* yfinance
* Pytest

## Methodology

### Data Collection

Historical adjusted stock price data was retrieved using Yahoo Finance through the `yfinance` Python library.

### Portfolio Construction

An equally weighted portfolio was constructed using five technology stocks, with each asset assigned a weight of 20%.

The portfolio uses daily rebalancing when calculating daily portfolio returns.

### Financial Performance Metrics

The following metrics were calculated:

| Metric                | Purpose                                               |
| --------------------- | ----------------------------------------------------- |
| Daily Returns         | Measures daily percentage price changes.              |
| Cumulative Returns    | Measures compounded investment performance.           |
| Annualised Return     | Estimates annual investment performance.              |
| Annualised Volatility | Measures variability in returns.                      |
| Sharpe Ratio          | Evaluates returns relative to risk.                   |
| Maximum Drawdown      | Measures the largest peak-to-trough decline.          |
| Beta                  | Measures sensitivity to benchmark movements.          |
| Alpha                 | Estimates performance relative to the CAPM benchmark. |

The analysis assumes an annual risk-free rate of 4%.

Annualised volatility uses 252 trading days.

## Key Results

| Metric                | Portfolio | S&P 500 |
| --------------------- | --------: | ------: |
| Cumulative Return     |   268.40% |  84.98% |
| Annualised Return     |    30.19% |  13.80% |
| Annualised Volatility |    28.22% |  16.96% |
| Sharpe Ratio          |    0.9307 |  0.5824 |
| Maximum Drawdown      |   -41.83% | -25.43% |

Additional portfolio metrics:

* **Beta:** 1.4634
* **Alpha:** 11.85%

### Interpretation

The equally weighted technology portfolio achieved a higher historical return than the S&P 500 over the analysed period.

However, it also experienced higher volatility and a larger maximum drawdown.

Its beta of 1.4634 indicates greater sensitivity to benchmark movements.

Historical performance does not guarantee future results. The analysis does not account for transaction costs, taxes or other real-world trading expenses.

## Project Structure

```text
stock-market-data-analysis/
│
├── data/
├── figures/
├── src/
│   ├── analysis.py
│   ├── download_data.py
│   ├── test_analysis.py
│   └── test_calculations.py
│
├── .gitignore
└── README.md
```

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/vunene28/stock-market-data-analysis.git
```

Navigate into the project:

```bash
cd stock-market-data-analysis
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install numpy pandas matplotlib seaborn yfinance pytest
```

Run the analysis:

```bash
python src/download_data.py
```

Run automated tests:

```bash
python -m pytest -vv
```

## Testing

The project includes six automated tests using Pytest:

* Daily returns
* Cumulative returns
* Annualised volatility
* Maximum drawdown
* Beta
* Sharpe ratio

**Current test status: 6 tests passed.**

## Future Improvements

* Implement Markowitz Mean-Variance Portfolio Optimisation.
* Calculate Value at Risk (VaR) and Conditional Value at Risk (CVaR).
* Introduce rolling volatility and rolling Sharpe ratio analysis.
* Explore Monte Carlo simulations.
* Develop a portfolio performance dashboard.
* Compare alternative portfolio weighting strategies.

## Author

Developed as part of my exploration of quantitative finance, financial engineering and data-driven investment analysis.

**GitHub:** [vunene28](https://github.com/vunene28)
