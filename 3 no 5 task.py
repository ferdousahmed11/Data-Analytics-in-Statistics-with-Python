import numpy as np

# Task-5
# Measures of Central Tendency
grouped_data_values = []
grouped_data_frequencies = []

for interval, frequency in grouped_data.items():
    grouped_data_values.append(interval)
    grouped_data_frequencies.append(frequency)

mean_am_grouped = np.average(grouped_data_values, weights=grouped_data_frequencies)
mean_gm_grouped = statistics.geometric_mean(grouped_data_values)
mean_hm_grouped = statistics.harmonic_mean(grouped_data_values)
mean_qm_grouped = np.percentile(grouped_data_values, 50, interpolation='linear', axis=None)

# Measures of Spread
median_grouped = np.percentile(grouped_data_values, 50, interpolation='linear', axis=None)
quartiles_grouped = np.percentile(grouped_data_values, [25, 50, 75], interpolation='linear', axis=None)
deciles_grouped = np.percentile(grouped_data_values, np.arange(10, 100, 10), interpolation='linear', axis=None)
percentiles_grouped = np.percentile(grouped_data_values, np.arange(1, 100), interpolation='linear', axis=None)

# Mode
mode_grouped = grouped_data_values[np.argmax(grouped_data_frequencies)]

# Range
data_range_grouped = max(grouped_data_values) - min(grouped_data_values)

# Interquartile Range
iqr_grouped = quartiles_grouped[2] - quartiles_grouped[0]

# Quartile Deviation
quartile_deviation_grouped = iqr_grouped / 2

# Mean Deviation
mean_deviation_grouped = np.average(np.abs(np.subtract(grouped_data_values, mean_am_grouped)), weights=grouped_data_frequencies)

# Standard Deviation
standard_deviation_grouped = np.sqrt(np.average((grouped_data_values - mean_am_grouped)**2, weights=grouped_data_frequencies))

# Skewness and Kurtosis
skewness_grouped = skew(grouped_data_values, bias=False)
kurtosis_value_grouped = kurtosis(grouped_data_values, fisher=False)

print("Mean (AM) (Grouped):", mean_am_grouped)
print("Mean (GM) (Grouped):", mean_gm_grouped)
print("Mean (HM) (Grouped):", mean_hm_grouped)
print("Mean (QM) (Grouped):", mean_qm_grouped)
print("Median (Grouped):", median_grouped)
print("Quartiles (Grouped):", quartiles_grouped)
print("Deciles (Grouped):", deciles_grouped)
print("Percentiles (Grouped):", percentiles_grouped)
print("Mode (Grouped):", mode_grouped)
print("Range (Grouped):", data_range_grouped)
print("Interquartile Range (Grouped):", iqr_grouped)
print("Quartile Deviation (Grouped):", quartile_deviation_grouped)
print("Mean Deviation (Grouped):", mean_deviation_grouped)
print("Standard Deviation (Grouped):", standard_deviation_grouped)
print("Skewness (Grouped):", skewness_grouped)
print("Kurtosis (Grouped):", kurtosis_value_grouped)
