def generate_combinations():
    return [(str(i).zfill(2), str(j).zfill(2)) for i in range(1, 90) for j in range(i + 1, 90)]


for i, j in generate_combinations():
    print("{}, {}".format(i, j), end=", ")
