# Problem 4: Define inclusive and exclusive method and convert the given data into group data

# Given data
marks_selected = [
    78, 70, 80, 52, 91, 47, 92, 34, 31, 73,
    64, 40, 35, 70, 67, 73, 99, 76, 53, 53,
    31, 98, 71, 94, 53, 98, 43, 36, 97, 44,
    92, 91, 89, 80, 57, 78, 58, 76, 65, 99,
    40, 68, 95, 36, 71, 55, 91, 98, 93, 35,
    89, 39, 58, 41, 90, 76, 60, 74, 89, 74,
    84, 87, 77, 57, 56, 68, 86, 69, 31, 77
]

# Inclusive and Exclusive Grouping
grouped_data_inclusive = {}
grouped_data_exclusive = {}

# Assuming intervals of width 10
for num in marks_selected:
    interval_inclusive = (num // 10) * 10
    interval_exclusive = ((num - 1) // 10) * 10 + 1
    if interval_inclusive in grouped_data_inclusive:
        grouped_data_inclusive[interval_inclusive] += 1
    else:
        grouped_data_inclusive[interval_inclusive] = 1

    if interval_exclusive in grouped_data_exclusive:
        grouped_data_exclusive[interval_exclusive] += 1
    else:
        grouped_data_exclusive[interval_exclusive] = 1

print("Inclusive Grouped Data:")
for interval, frequency in sorted(grouped_data_inclusive.items()):
    print(f"{interval} - {interval + 9}: {frequency}")

print("\nExclusive Grouped Data:")
for interval, frequency in sorted(grouped_data_exclusive.items()):
    print(f"{interval} - {interval + 9}: {frequency}")
