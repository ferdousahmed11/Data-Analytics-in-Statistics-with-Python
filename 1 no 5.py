import numpy as np

# Problem 5: Calculate the Mean, Quartile, Decile, Percentile, Skewness, Moment, and Kurtosis of the calculated group data

# Calculating the statistics for grouped data
grouped_data_values = list(grouped_data_inclusive.keys())
grouped_data_frequencies = list(grouped_data_inclusive.values())

# Measures of Central Tendency
mean_grouped = np.average(grouped_data_values, weights=grouped_data_frequencies)
median_grouped = np.percentile(grouped_data_values, 50, interpolation='linear')
quartiles_grouped = np.percentile(grouped_data_values, [25, 50, 75], interpolation='linear')
deciles_grouped = np.percentile(grouped_data_values, np.arange(10, 100, 10), interpolation='linear')
percentiles_grouped = np.percentile(grouped_data_values, np.arange(1, 100), interpolation='linear')

# Skewness and Kurtosis
skewness_grouped = np.mean((grouped_data_values - mean_grouped) ** 3) / np.power(np.var(grouped_data_values), 1.5)
kurtosis_grouped = np.mean((grouped_data_values - mean_grouped) ** 4) / np.power(np.var(grouped_data_values), 2)

print("Mean (Grouped):", mean_grouped)
print("Median (Grouped):", median_grouped)
print("Quartiles (Grouped):", quartiles_grouped)
print("Deciles (Grouped):", deciles_grouped)
print("Percentiles (Grouped):", percentiles_grouped)
print("Skewness (Grouped):", skewness_grouped)
print("Kurtosis (Grouped):", kurtosis_grouped)
