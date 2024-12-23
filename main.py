""""
import matplotlib.pyplot as plt
from stock_data_utils import fetch_stock_data, load_clean_stock_data
from stationarity_test import adf_test  # Import the ADF test function
from data_transform import transform_and_test_stationarity  # Import the transformation function
from autofit_arima_model import fit_auto_arima, plot_forecast  # Import ARIMA functions

# Get user inputs
ticker = input("Enter the ticker symbol of the stock (e.g., 'RELIANCE.NS'): ")
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")
filename = input("Enter the filename to save the data (e.g., 'stock_data.csv'): ")

# Step 1: Fetch and save the stock data
fetch_stock_data(ticker, start_date, end_date, filename)

# Step 2: Load and clean the stock data
stock_data = load_clean_stock_data(filename)

if stock_data is not None:
    # Print column names and the first few rows for verification
    print("Column Names:", stock_data.columns)
    print(stock_data.head())

    # Step 3: Perform ADF test on 'Close' prices
    print("\nADF Test Result for Closing Prices:")
    adf_test(stock_data['Close'])

    # Step 4: Plot the closing prices
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data['Close'], label=f'Closing Prices of {ticker}')
    plt.title(f'Closing Prices of {ticker} from {start_date} to {end_date}')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Step 5: Transform and test stationarity of the data
    print("\n--- Performing Data Transformations and Stationarity Tests ---\n")
    stationary_series = transform_and_test_stationarity(filename)

    if stationary_series is not None:
        # Step 6: Fit ARIMA model to the stationary series
        print("\nFitting ARIMA model on the stationary series:")
        arima_model = fit_auto_arima(stationary_series, seasonal=False)
        
        # Print the ARIMA model summary
        print(arima_model.summary())
        
        # Step 7: Forecast and visualize
        print("\nGenerating Forecast...")
        plot_forecast(arima_model, stationary_series, steps=30)

else:
    print("Could not load data. Please check the input and file.")

"""
import matplotlib.pyplot as plt
from stock_data_utils import fetch_stock_data, load_clean_stock_data
from stationarity_test import adf_test  # Import the ADF test function
from data_transform import transform_and_test_stationarity  # Import the transformation function
from autofit_arima_model import fit_auto_arima  # Import ARIMA function
from forecast_future_values import forecast_log_diff_and_prices # Import forecasting function

# Get user inputs
ticker = input("Enter the ticker symbol of the stock (e.g., 'RELIANCE.NS'): ")
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")
filename = input("Enter the filename to save the data (e.g., 'stock_data.csv'): ")

# Step 1: Fetch and save the stock data
fetch_stock_data(ticker, start_date, end_date, filename)

# Step 2: Load and clean the stock data
stock_data = load_clean_stock_data(filename)

if stock_data is not None:
    # Print column names and the first few rows for verification
    print("Column Names:", stock_data.columns)
    print(stock_data.head())

    # Step 3: Perform ADF test on 'Close' prices
    print("\nADF Test Result for Closing Prices:")
    adf_test(stock_data['Close'])

    # Step 4: Plot the closing prices
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data['Close'], label=f'Closing Prices of {ticker}')
    plt.title(f'Closing Prices of {ticker} from {start_date} to {end_date}')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Step 5: Transform and test stationarity of the data
    print("\n--- Performing Data Transformations and Stationarity Tests ---\n")
    stationary_series = transform_and_test_stationarity(filename)

    if stationary_series is not None:
        # Step 6: Fit ARIMA model to the stationary series
        print("\nFitting ARIMA model on the stationary series:")
        arima_model = fit_auto_arima(stationary_series, seasonal=False)
        
        # Print the ARIMA model summary
        print(arima_model.summary())
        
        # Step 7: Forecast and visualize future values
        print("\nGenerating Forecast...")
        forecast_series = forecast_log_diff_and_prices(arima_model, stationary_series, forecast_periods=30)
        print(f"Forecasted Values:\n{forecast_series}")

else:
    print("Could not load data. Please check the input and file.")
