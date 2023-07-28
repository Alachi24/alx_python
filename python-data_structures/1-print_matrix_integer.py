def print_matrix_integer(matrix=[[]]):
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    # Iterate through each row and print the elements with the specified format
    for row in matrix:
        for col_idx, value in enumerate(row):
            # Print each element with the specified format and separate them with spaces
            print("{:d}".format(value),
                  end=" " if col_idx < num_cols - 1 else "")
        # Move to the next row after printing all elements in the current row
        print()


# Test the function with an example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
