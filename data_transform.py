import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from stationarity_test import adf_test  # Import the ADF test function

def plot_series(series, title):
    """
    Helper function to plot a time series.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(series, label=title)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()
"""
def transform_and_test_stationarity(filename):
    
   # Read the CSV file, apply transformations, and test stationarity using ADF test.

   # Parameters:
    #    filename (str): Path to the CSV file containing stock data.

   # Returns:
    #    None
    
    # Step 1: Read the CSV file
    df = pd.read_csv(filename)

    # Step 2: Parse the date column
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
"""
def transform_and_test_stationarity(filename):
    # Step 1: Load CSV properly by skipping the invalid rows
    try:
         # Load CSV, skipping unnecessary rows and setting appropriate headers
        #df = pd.read_csv(filename, skiprows=3, index_col=0, parse_dates=True)
         # Manually assign column names
       # df.columns = ['Price', 'Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']
        column_names = ['Price', 'Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']
        df = pd.read_csv(filename, skiprows=3, names=column_names, index_col=0, parse_dates=True)


        # Verify the structure of the DataFrame
        print("Column Names:", df.columns)
        print("DataFrame Head:\n", df.head())
    except Exception as e:
        print("Column Names:", df.columns)  # Debug column names
        print("Error reading the CSV file:", e)
        return
  # Check if 'Close' column exists
    if 'Close' not in df.columns:
        print("'Close' column not found. Available columns are:", df.columns)
        return
    print("Cleaned DataFrame:\n", df.head())
#--------------------------------------------------------


#-----------------------------------------
    # Use index as Date (since 'Date' column is now the index)
    closing_prices = df['Close']
    print("Closing Prices Head:\n", closing_prices.head())

    # Step 2: Perform transformations and ADF tests
    plot_series(closing_prices, 'Original Closing Prices')
    print("\nADF Test Result for Original Closing Prices:")
    adf_test(closing_prices)

    # First Difference
    first_difference = closing_prices.diff().dropna()
    plot_series(first_difference, 'First Difference of Closing Prices')
    print("\nADF Test Result for First Difference of Closing Prices:")
    adf_test(first_difference)

    # Log Transformation
    log_transformation = np.log(closing_prices).dropna()
    plot_series(log_transformation, 'Log Transformation of Closing Prices')
    print("\nADF Test Result for Log Transformation of Closing Prices:")
    adf_test(log_transformation)

    # Log Difference
    log_difference = log_transformation.diff().dropna()
    plot_series(log_difference, 'Log Difference of Closing Prices')
    print("\nADF Test Result for Log Difference of Closing Prices:")
    adf_test(log_difference)

