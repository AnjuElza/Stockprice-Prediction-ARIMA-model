import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def load_stock_data(filename):
    """
    Load and clean stock data from a CSV file.

    Parameters:
    - filename: String, path to the CSV file.

    Returns:
    - Pandas DataFrame with cleaned data.
    """

# Define column names manually
column_names = ["Date", "Price", "Adj Close", "Close", "High", "Low", "Open", "Volume"]

# Function to fetch and save stock data
def fetch_stock_data(ticker, start_date, end_date, filename):
    # Fetch data from Yahoo Finance
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    
    # Save data to CSV
    stock_data.to_csv(filename)
    print(f"Data saved to {filename}")

    # Get user inputs
    ticker = input("Enter the ticker symbol of the Nifty 50 stock (e.g., 'RELIANCE.NS'): ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    filename = input("Enter the filename to save the data (e.g., 'stock_data.csv'): ")

    # Validate date format
    try:
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        exit()

    # Fetch and save stock data
    fetch_stock_data(ticker, start_date, end_date, filename)

# Read the saved CSV file
# stock_data = pd.read_csv(filename, index_col='Date', parse_dates=True)
#try:
#    stock_data = pd.read_csv(
#        filename,
#        parse_dates=True,  # Automatically parse dates
#        index_col=0        # Use the first column (Date) as the index
 #   )

#    print("Columns in the CSV:", stock_data.columns)
#except FileNotFoundError:
#    print(f"Error: The file {filename} does not exist.")
#    exit()

# Read the CSV file, skipping the first two rows
#stock_data = pd.read_csv(
 #   filename,
 #   skiprows=2,               # Skip the first two rows
 #   index_col="Date",         # Use 'Date' as the index
 #   parse_dates=True          # Parse the 'Date' column as datetime
 #)
# Read the CSV file, skipping the first two rows and assigning proper column names
    stock_data = pd.read_csv(
     filename,
     skiprows=2,                # Skip the first two rows
    names=column_names,        # Assign custom column names
    index_col="Date",          # Use 'Date' as the index
    parse_dates=True           # Parse 'Date' column as datetime
    )

    # Clean up column names by stripping whitespace
    stock_data.columns = stock_data.columns.str.strip()

    # Print the column names and first few rows for verification
    print("Column Names:", stock_data.columns)
    print(stock_data.head())


    # Check for missing or invalid values in the 'Close' column
    print(stock_data['Close'].isna().sum())  # Check for missing values
    print(stock_data['Close'].dtype)        # Check data type

    # Drop rows with missing 'Close' values if necessary
    stock_data = stock_data.dropna(subset=['Close'])

# Convert 'Close' to numeric (if needed)
stock_data['Close'] = pd.to_numeric(stock_data['Close'], errors='coerce')


# Plot the closing prices
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label=f'Closing Prices of {ticker}')
plt.title(f'Closing Prices of {ticker} from {start_date} to {end_date}')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)
plt.show() 

stock_data.columns = stock_data.columns.str.strip()  # Clean column names
return stock_data