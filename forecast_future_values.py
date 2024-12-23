import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def forecast_log_diff_and_prices(model, original_series, log_difference, forecast_periods=30):
    """
    Forecast future stock prices and log differences using the fitted ARIMA model.
    
    Parameters:
    - model: The fitted ARIMA model
    - original_series: Original stock price series
    - log_difference: Stationary time series (log difference)
    - forecast_periods: Number of future periods to forecast
    
    Returns:
    - forecast_log_diff: Forecasted log differences (Pandas Series)
    - forecast_stock_prices: Forecasted stock prices (Pandas Series)
    """
    # Step 1: Generate forecast for log differences
    forecast = model.predict(n_periods=forecast_periods)
    
    # Step 2: Create a series for the forecasted log differences
    forecast_index = pd.date_range(
        start=log_difference.index[-1], 
        periods=forecast_periods + 1, 
        freq='D', 
        inclusive='right'
    )[1:]
    forecast_log_diff = pd.Series(forecast, index=forecast_index)
    
    # Step 3: Convert log differences to stock prices
    last_original_price = original_series.iloc[-1]  # Get the last observed stock price
    forecast_stock_prices = forecast_log_diff.cumsum() + np.log(last_original_price)
    forecast_stock_prices = np.exp(forecast_stock_prices)

    # Step 4: Plot log differences
    plt.figure(figsize=(10, 5))
    plt.plot(log_difference, label='Log Difference of Closing Prices')
    plt.plot(forecast_log_diff, label='Forecasted Log Differences', color='red')
    plt.title('Log Difference of Closing Prices with Forecasted Values')
    plt.xlabel('Date')
    plt.ylabel('Log Difference of Closing Price')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Step 5: Plot original stock prices and forecasted prices
    plt.figure(figsize=(10, 5))
    plt.plot(original_series, label='Original Closing Prices')
    plt.plot(forecast_stock_prices, label='Forecasted Stock Prices', color='red')
    plt.title('Closing Prices with Forecasted Values')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.grid(True)
    plt.show()

    return forecast_log_diff, forecast_stock_prices
