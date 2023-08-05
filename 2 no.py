import numpy as np

# Create a list of prices
prices = [20, 40, 40, 60, 60, 60, 60, 60, 70, 70]

# Calculate the median price
median_price = np.median(prices)

# Print the median price
print("Median price:", median_price)



# Create a list of prices
prices = [20, 40, 40, 60, 60, 60, 60, 60, 70, 70]

# Calculate the maximum price
maximum_price = np.max(prices)

# Check the prediction of the broker
if maximum_price <= 70:
    print("Broker's prediction is correct.")
else:
    print("Broker's prediction is incorrect.")
