def parse_columns(file_path):
    left_column = []
    right_column = []
    with open(file_path, "r") as file:
        for line in file:
            if line.strip():
                left, right = map(int, line.split())
                left_column.append(left)
                right_column.append(right)
    return left_column, right_column