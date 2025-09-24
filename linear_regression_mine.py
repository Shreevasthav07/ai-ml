#implement linear regression using sample dataset
import numpy as np
import matplotlib.pyplot as plt

# Sample house price dataset (size in sqft, price in $1000)
size_sqft = np.array([750, 800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400])
price_k = np.array([150, 160, 165, 170, 180, 185, 195, 210, 220, 230])

# Number of samples
n = len(size_sqft)

# Calculate means
mean_x = np.mean(size_sqft)
mean_y = np.mean(price_k)

# Calculate slope (beta1) and intercept (beta0)
numerator = np.sum((size_sqft - mean_x) * (price_k - mean_y))
denominator = np.sum((size_sqft - mean_x) ** 2)

slope = numerator / denominator
intercept = mean_y - slope * mean_x

print(f"Fitted model: price_k = {slope:.2f} * size_sqft + {intercept:.2f}")

# Prediction function
def predict(x):
    return slope * x + intercept

# Predicted prices
predicted_prices = predict(size_sqft)

# Plotting
plt.scatter(size_sqft, price_k, color='blue', label='Actual Prices')
plt.plot(size_sqft, predicted_prices, color='red', label='Regression Line')

plt.xlabel('Size (sqft)')
plt.ylabel('Price ($1000)')
plt.title('House Price Prediction using Linear Regression')
plt.legend()
plt.show()
