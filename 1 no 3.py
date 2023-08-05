# Problem 3: What do you mean by group and ungroup data? Find out the frequency of given data

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

# Grouping the data (assuming intervals of width 10)
grouped_data = {}
for num in marks_selected:
    interval = (num // 10) * 10
    if interval in grouped_data:
        grouped_data[interval] += 1
    else:
        grouped_data[interval] = 1

print("Grouped Data:")
for interval, frequency in sorted(grouped_data.items()):
    print(f"{interval} - {interval + 9}: {frequency}")
