import pandas as pd
import yfinance as yf
from datetime import datetime

# Define column names manually
COLUMN_NAMES = ["Date", "Price", "Adj Close", "Close", "High", "Low", "Open", "Volume"]

def fetch_stock_data(ticker, start_date, end_date, filename):
    """
    Fetch stock data for a given ticker and date range and save it to a CSV file.
    """
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        stock_data.to_csv(filename)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error fetching stock data: {e}")

def load_clean_stock_data(filename):
    """
    Load stock data from a CSV file, clean it, and return a Pandas DataFrame.
    """
    try:
        # Read the CSV file, skipping the first two rows and assigning column names
        stock_data = pd.read_csv(
            filename,
            skiprows=2,                # Skip the first two rows
            names=COLUMN_NAMES,        # Assign custom column names
            index_col="Date",          # Use 'Date' as the index
            parse_dates=True           # Parse 'Date' column as datetime
        )

        # Clean up column names and drop missing 'Close' values
        stock_data.columns = stock_data.columns.str.strip()
        stock_data = stock_data.dropna(subset=['Close'])
        stock_data['Close'] = pd.to_numeric(stock_data['Close'], errors='coerce')

        print("Data loaded and cleaned successfully.")
        return stock_data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
