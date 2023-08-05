import statistics
from scipy.stats import skew, kurtosis

# Task-3
# Measures of Central Tendency
mean_am = statistics.mean(data_list)
mean_gm = statistics.geometric_mean(data_list)
mean_hm = statistics.harmonic_mean(data_list)
mean_qm = statistics.median(data_list)

# Measures of Spread
median = statistics.median(data_list)
quartiles = statistics.quantiles(data_list, n=4)
deciles = statistics.quantiles(data_list, n=10)
percentiles = statistics.quantiles(data_list, n=100)

# Mode
mode = statistics.mode(data_list)

# Range
data_range = max(data_list) - min(data_list)

# Interquartile Range
iqr = quartiles[2] - quartiles[0]

# Quartile Deviation
quartile_deviation = iqr / 2

# Mean Deviation
mean_deviation = statistics.mean([abs(x - mean_am) for x in data_list])

# Standard Deviation
standard_deviation = statistics.stdev(data_list)

# Skewness and Kurtosis
skewness = skew(data_list)
kurtosis_value = kurtosis(data_list)

print("Mean (AM):", mean_am)
print("Mean (GM):", mean_gm)
print("Mean (HM):", mean_hm)
print("Mean (QM):", mean_qm)
print("Median:", median)
print("Quartiles:", quartiles)
print("Deciles:", deciles)
print("Percentiles:", percentiles)
print("Mode:", mode)
print("Range:", data_range)
print("Interquartile Range:", iqr)
print("Quartile Deviation:", quartile_deviation)
print("Mean Deviation:", mean_deviation)
print("Standard Deviation:", standard_deviation)
print("Skewness:", skewness)
print("Kurtosis:", kurtosis_value)
