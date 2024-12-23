from statsmodels.tsa.stattools import adfuller

def adf_test(series):
    """
    Perform Augmented Dickey-Fuller (ADF) test on a time series.

    Parameters:
        series (pd.Series): The time series data to test.

    Prints:
        ADF Statistic, p-value, and critical values.
    """
    print("Performing Augmented Dickey-Fuller Test...")
    result = adfuller(series, autolag='AIC')

    print(f"ADF Statistic: {result[0]}")
    print(f"p-value: {result[1]}")
    print("Critical Values:")
    for key, value in result[4].items():
        print(f"   {key}: {value}")
    
    if result[1] < 0.05:
        print("Result: The time series is stationary (reject null hypothesis).")
    else:
        print("Result: The time series is non-stationary (fail to reject null hypothesis).")
