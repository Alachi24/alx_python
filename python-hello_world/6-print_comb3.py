def generate_combinations():
    combinations = [(i, j) for i in range(89) for j in range(89) if i != j]
    return combinations


all_combinations = generate_combinations()

for combinations in all_combinations:
    print(f"{combinations[0]}, {combinations[1]}", end=", ")
