def generate_combinations():
    for i in range(1, 10):
        for j in range(i + 1, 10):
            print("{:02}, {:02}".format(i, j), end=", ")


for j in range(1, 91):
    print("{:02}, {:02}".format(", ", j), end=", ")
