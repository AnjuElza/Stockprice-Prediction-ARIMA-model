"""
# Auto-fit ARIMA model on log difference (or any stationary series)

print("\nFitting ARIMA model on Log Difference of Closing Prices:")

    model = auto_arima(log_difference, seasonal=False, trace=True, error_action='ignore', suppress_warnings=True)

    print(model.summary())
    """
from pmdarima import auto_arima
import matplotlib.pyplot as plt

def fit_auto_arima(stationary_series, seasonal=False, m=1):
    """
    Automatically fits an ARIMA model to the provided stationary series.

    Parameters:
        stationary_series (pd.Series): The stationary time series to model.
        seasonal (bool): Whether to consider seasonal ARIMA. Default is False.
        m (int): The number of periods in a seasonal cycle. Default is 1.

    Returns:
        model (ARIMA): The fitted ARIMA model.
    """
    print("\nFitting ARIMA model on the stationary series:")
    try:
        model = auto_arima(
            stationary_series,
            seasonal=seasonal,
            m=m,
            trace=True,
            error_action='ignore',
            suppress_warnings=True,
            stepwise=True
        )
        print("\nModel successfully fitted:")
        print(model.summary())
        return model
    except Exception as e:
        print(f"Error fitting ARIMA model: {e}")
        return None


def plot_forecast(model, stationary_series, steps=30):
    """
    Generates and plots the forecast from the ARIMA model.

    Parameters:
        model (ARIMA): The fitted ARIMA model.
        stationary_series (pd.Series): The original stationary series.
        steps (int): Number of steps to forecast. Default is 30.

    Returns:
        None
    """
    if model is None:
        print("No model available for forecasting.")
        return

    try:
        # Generate forecasts
        forecast, conf_int = model.predict(n_periods=steps, return_conf_int=True)

        # Create forecast index
        forecast_index = range(len(stationary_series), len(stationary_series) + steps)

        # Plot the results
        plt.figure(figsize=(12, 6))
        plt.plot(stationary_series, label='Historical Data', color='blue')
        plt.plot(forecast_index, forecast, label='Forecast', color='orange')
        plt.fill_between(
            forecast_index,
            conf_int[:, 0],
            conf_int[:, 1],
            color='orange',
            alpha=0.2,
            label='Confidence Interval'
        )
        plt.title("ARIMA Model Forecast")
        plt.xlabel("Time Steps")
        plt.ylabel("Values")
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Error generating forecast: {e}")
