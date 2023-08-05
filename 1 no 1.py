# Problem 1: Define Population and Sample

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

# Population: All students who were evaluated by the BUP (87 students)
population = range(1, 88)

# Sample: Selected marks from 70 students
sample = marks_selected

print("Population:", population)
print("Sample:", sample)
