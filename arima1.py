import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import adfuller

from statsmodels.tsa.seasonal import seasonal_decompose

from pmdarima import auto_arima

 
# Function to perform ADF test and print the result with analysis

def adf_test(timeseries):

    result = adfuller(timeseries)

    adf_statistic = result[0]

    p_value = result[1]

    critical_values = result[4]

    print('ADF Statistic: %f' % adf_statistic)

    print('p-value: %f' % p_value)

    print('Critical Values:')

    for key, value in critical_values.items():

        print('\t%s: %.3f' % (key, value))

 
    if p_value < 0.05:

        print("The p-value is less than 0.05, so we reject the null hypothesis. The time series is stationary.")

    else:

        print("The p-value is greater than 0.05, so we fail to reject the null hypothesis. The time series is non-stationary.")

   
    for key, value in critical_values.items():

        if adf_statistic < value:

            print(f"The ADF statistic is less than the {key} critical value. We reject the null hypothesis at the {key} level. The time series is stationary.")

        else:

            print(f"The ADF statistic is greater than the {key} critical value. We fail to reject the null hypothesis at the {key} level. The time series is non-stationary.")


# Function to plot the time series

def plot_series(timeseries, title):

    plt.figure(figsize=(10, 5))

    plt.plot(timeseries, label=title)

    plt.title(title)

    plt.xlabel('Date')

    plt.ylabel('Value')

    plt.legend()

    plt.grid(True)

    plt.show()

 

# Function to read the CSV file, apply transformations, and fit ARIMA model

def transform_and_test_stationarity(filename):

    # Read the CSV file

    df = pd.read_csv(filename)

   

    # Parse the date column (assuming the date column is named 'Date')

    df['Date'] = pd.to_datetime(df['Date'])

    df.set_index('Date', inplace=True)

   
    # Extract the closing prices

    closing_prices = df['Close']
  

    # Original Series

    plot_series(closing_prices, 'Original Closing Prices')

    print("\nADF Test Result for Original Closing Prices:")

    adf_test(closing_prices)

 

    # 1. Differencing

    first_difference = closing_prices.diff().dropna()

    plot_series(first_difference, 'First Difference of Closing Prices')

    print("\nADF Test Result for First Difference of Closing Prices:")

    adf_test(first_difference)


    # 2. Log Transformation

    log_transformation = np.log(closing_prices).dropna()

    plot_series(log_transformation, 'Log Transformation of Closing Prices')

    print("\nADF Test Result for Log Transformation of Closing Prices:")

    adf_test(log_transformation)

 

    # 3. Seasonal Decomposition

    result = seasonal_decompose(closing_prices, model='additive', period=30)

    seasonal_adjusted = closing_prices - result.seasonal

    plot_series(seasonal_adjusted.dropna(), 'Seasonally Adjusted Closing Prices')

    print("\nADF Test Result for Seasonally Adjusted Closing Prices:")

    adf_test(seasonal_adjusted.dropna())

     # 4. Log Difference

    log_difference = log_transformation.diff().dropna()

    plot_series(log_difference, 'Log Difference of Closing Prices')

    print("\nADF Test Result for Log Difference of Closing Prices:")

    adf_test(log_difference)


    # Auto-fit ARIMA model on log difference (or any stationary series)

    print("\nFitting ARIMA model on Log Difference of Closing Prices:")

    model = auto_arima(log_difference, seasonal=False, trace=True, error_action='ignore', suppress_warnings=True)

    print(model.summary())

 

    # Forecast future values

    forecast_periods = 30

    forecast = model.predict(n_periods=forecast_periods)

 
    # Create a series for the forecast

    forecast_index = pd.date_range(start=log_difference.index[-1], periods=forecast_periods + 1, freq='D', inclusive='right')[1:]

    forecast_series = pd.Series(forecast, index=forecast_index)


    # Plot the original and forecasted values

    plt.figure(figsize=(10, 5))

    plt.plot(log_difference, label='Log Difference of Closing Prices')

    plt.plot(forecast_series, label='Forecasted Values', color='red')

    plt.title('Log Difference of Closing Prices with Forecasted Values')

    plt.xlabel('Date')

    plt.ylabel('Log Difference of Closing Price')

    plt.legend()

    plt.grid(True)

    plt.show()

 # Example usage

filename = input("Enter the filename of the CSV file to read (e.g., 'stock_data.csv'): ")

transform_and_test_stationarity(filename) 