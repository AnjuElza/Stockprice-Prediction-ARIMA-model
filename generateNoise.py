import numpy as np
import matplotlib.pyplot as plt

# Generate white noise
np.random.seed(0)
white_noise = np.random.normal(0, 1, 1000)

# Plot the white noise
plt.figure(figsize=(10, 6))
plt.plot(white_noise)
plt.title('White Noise')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()

# Plot the autocorrelation function (ACF)
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(white_noise, lags=40)
plt.title('Autocorrelation Function (ACF) of White Noise')
plt.show()