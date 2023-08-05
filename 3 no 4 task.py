# Task-4
# Assuming intervals of width 10, starting from 30 to 100
grouped_data = {}
for num in data_list:
    interval = (num // 10) * 10
    if interval in grouped_data:
        grouped_data[interval] += 1
    else:
        grouped_data[interval] = 1

print("Grouped Data:")
for interval, frequency in sorted(grouped_data.items()):
    print(f"{interval} - {interval + 9}: {frequency}")
