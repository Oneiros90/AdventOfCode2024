import utilities.files

file_path = "inputs/locations.txt"
left, right = utilities.files.parse_columns(file_path)
left.sort()
right.sort()
similarity_scores = []
frequencies = {id: right.count(id) for id in set(right)}
for i in range(0, len(left)):
    id = left[i]
    frequency = 0 if id not in frequencies else frequencies[id]
    similarity_score = id * frequency
    similarity_scores.append(similarity_score)
result = sum(similarity_scores)
print(result)