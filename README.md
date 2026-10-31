# Project Overview

This project is a quantitative risk simulator designed for the Ethiopian Securities Exchange (ESX). As the ESX is a newly established market, retail investors lack institutional-grade tools to understand portfolio risk. This Python-based engine uses Geometric Brownian Motion (GBM) and Cholesky Decomposition to simulate 10,000 possible future scenarios for a diversified 5-asset portfolio

The Problem

When investing in emerging markets, volatility and correlation are highly unpredictable. Standard financial models often treat asset prices independently, which drastically underestimates risk. When the market crashes, assets tend to fall together

The Solution

This model accounts for the correlation matrix of a portfolio containing five sectors:

Technology: Alphabet (GOOGL)

Healthcare: Johnson & Johnson (JNJ)

Financials: JPMorgan Chase (JPM)

Consumer Staples: Walmart (WMT)

Energy: Exxon Mobil (XOM)

By applying a Cholesky Decomposition to the covariance matrix, the engine generates correlated random shocks, ensuring the simulated asset paths behave realistically

Key Outputs

Median Expected Path: The most likely outcome for the portfolio over a 1-year horizon.

Value at Risk (VaR): The 5th percentile worst-case scenario. This tells the investor the maximum expected loss with 95% confidence.

Confidence Intervals: Visualizes the spread between the best and worst outcomes

Tech Stack

Python 3

NumPy (Linear algebra, matrix operations, and stochastic modeling)

Matplotlib (Data visualization and confidence interval shading)


How to Run

Clone this repository.

Install dependencies: pip install numpy matplotlib

Run the script: python portfolio_simulation.py






