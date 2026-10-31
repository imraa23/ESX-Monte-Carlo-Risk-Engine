import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 1. Set the parameters
initial_value = 100000 # Our portfolio starts at $100k
days = 252             # 1 year of trading
simulations = 10000    # 10,000 simulations

# 2. The Data from your Excel sheet (GOOGL, JNJ, JPM, WMT, XOM)
weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
expected_returns = np.array([0.12, 0.07, 0.09, 0.06, 0.08])
volatilities = np.array([0.25, 0.15, 0.20, 0.18, 0.22])

# 3. The Correlation Matrix
correlation_matrix = np.array([
    [1.0, 0.3, 0.4, 0.2, 0.1], 
    [0.3, 1.0, 0.3, 0.5, 0.2], 
    [0.4, 0.3, 1.0, 0.4, 0.3], 
    [0.2, 0.5, 0.4, 1.0, 0.2], 
    [0.1, 0.2, 0.3, 0.2, 1.0]  
])

# 4. Calculate the Covariance Matrix
cov_matrix = np.diag(volatilities) @ correlation_matrix @ np.diag(volatilities)

# 5. Generate Correlated Random Shocks
L = np.linalg.cholesky(cov_matrix)
dt = 1 / 252
uncorrelated_shocks = np.random.normal(0, 1, (days, 5, simulations))

# Multiplying by np.sqrt(dt) 
correlated_shocks = np.einsum('ij,tjs->tis', L, uncorrelated_shocks) * np.sqrt(dt)

# 6. Calculate Daily Returns for the Portfolio
daily_drift = (expected_returns - 0.5 * volatilities**2) * dt
daily_returns = daily_drift[None, :, None] + correlated_shocks

# Combine them using the weights
portfolio_returns = np.einsum('i,tis->ts', weights, daily_returns)

# 7. Calculate the Portfolio Value Paths
cumulative_returns = np.cumsum(portfolio_returns, axis=0)
portfolio_paths = initial_value * np.exp(cumulative_returns)
portfolio_paths = np.vstack([np.full(simulations, initial_value), portfolio_paths])

# 8. Plot
plt.style.use('dark_background') 
fig, ax = plt.subplots(figsize=(12, 6))

# Calculate percentiles for shading
percentile_5 = np.percentile(portfolio_paths, 5, axis=1)
percentile_95 = np.percentile(portfolio_paths, 95, axis=1)
median = np.median(portfolio_paths, axis=1)
x_axis = range(len(median)) 

#  few random paths 
ax.plot(portfolio_paths[:, :50], linewidth=0.7, alpha=0.15, color='#4da6ff')

#  Shade  90% Confidence Interval
ax.fill_between(x_axis, percentile_5, percentile_95, color='#00ffcc', alpha=0.15, label='90% Confidence Interval')

# Plot the outer bounds
ax.plot(percentile_95, color='#00ffcc', linewidth=1.5, label='95% Best Case')
ax.plot(percentile_5, color='#ff4d4d', linewidth=1.5, label='5% Worst Case (VaR)')

# Plot the Median
ax.plot(median, color='white', linewidth=2.5, label='Median Expected Path')

# Formatting
ax.set_title('Monte Carlo Simulation', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Annual Trading Days', fontsize=12)
ax.set_ylabel('Portfolio Value ', fontsize=12)
ax.grid(color='gray', linestyle='--', linewidth=0.3, alpha=0.5)
ax.legend(loc='upper left', frameon=True, facecolor='black', edgecolor='gray')

# Format Y-axis  show dollar signs
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))

plt.tight_layout()
plt.show()
