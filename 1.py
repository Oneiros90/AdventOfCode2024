import utilities.files

file_path = "inputs/locations.txt"
left, right = utilities.files.parse_columns(file_path)
left.sort()
right.sort()
differences = []
for i in range(0, len(left)):
    difference = abs(left[i] - right[i])
    differences.append(difference)
result = sum(differences)
print(result)