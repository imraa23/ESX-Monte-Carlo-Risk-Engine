
##  Project Overview
This project is a quantitative risk simulator designed for the **Ethiopian Securities Exchange (ESX)**. As the ESX is a newly established market, retail investors lack institutional-grade tools to understand portfolio risk. This Python-based engine uses **Geometric Brownian Motion (GBM)** and **Cholesky Decomposition** to simulate 10,000 possible future scenarios for a diversified 5-asset portfolio.

## ⚠️ Data Limitations and Future Adaptation
Because the Ethiopian Securities Exchange (ESX) launched in January 2025, it currently lacks sufficient historical price data to calculate accurate covariance matrices. Therefore, this engine is currently deployed as a **Proof of Concept** using highly liquid US equities (GOOGL, JNJ, JPM, WMT, XOM) from my simulated  portfolio. 

The mathematical framework—including the Cholesky Decomposition and Monte Carlo paths—is completely asset-agnostic. As the ESX matures and generates historical data, users can simply input ESX ticker symbols and their respective historical volatilities to run the exact same risk analysis on local Ethiopian stocks.


##  The Problem
When investing in emerging markets, volatility and correlation are highly unpredictable. Standard financial models often treat asset prices independently, which drastically underestimates risk. When the market crashes, assets tend to fall together. 

##  The Solution
This model accounts for the **correlation matrix** of a portfolio containing five sectors:
*   **Technology:** Alphabet (GOOGL)
*   **Healthcare:** Johnson & Johnson (JNJ)
*   **Financials:** JPMorgan Chase (JPM)
*   **Consumer Staples:** Walmart (WMT)
*   **Energy:** Exxon Mobil (XOM)

By applying a Cholesky Decomposition to the covariance matrix, the engine generates correlated random shocks, ensuring the simulated asset paths behave realistically.

##  Mathematical Underpinnings 

Here is the mathematical framework powering the simulation:

1. **Geometric Brownian Motion (GBM):** Stock prices are modeled using the stochastic differential equation: 
   `dS_t = μ S_t dt + σ S_t dW_t`
   Where `μ` is the expected drift, `σ` is the volatility, and `dW_t` is the Wiener process (random shock). By integrating this, we generate 10,000 unique price paths.

2. **Cholesky Decomposition:** Assets in a portfolio are not independent; they are correlated. To simulate this, I constructed a Covariance Matrix and decomposed it into a lower triangular matrix using the Cholesky formula (`A = LL^T`). This transforms independent random shocks into correlated shocks, ensuring that if Tech crashes, the Energy sector reacts realistically.

3. **Value at Risk (VaR):** By calculating the 5th percentile of the 10,000 simulated portfolio paths, the engine determines the portfolio's 95% VaR. This quantifies the maximum expected loss over a one-year horizon with 95% statistical confidence.

   
##  Key Outputs
*   **Median Expected Path:** The most likely outcome for the portfolio over a 1-year horizon.
*   **Value at Risk (VaR):** The 5th percentile worst-case scenario. This tells the investor the maximum expected loss with 95% confidence.
*   **Confidence Intervals:** Visualizes the spread between the best and worst outcomes.

##  Tech Stack
*   **Python 3**
*   **NumPy** (Linear algebra, matrix operations, and stochastic modeling)
*   **Matplotlib** (Data visualization and confidence interval shading)

##  How to Run
1. Clone this repository.
2. Install dependencies: `pip install numpy matplotlib`
3. Run the script: `python portfolio_simulation.py`






