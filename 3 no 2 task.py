# Task-2
data_list = []

with open("data.txt", "r") as file:
    for line in file:
        data_list.extend(map(int, line.split()))

print("Ungrouped Data List:", data_list)
