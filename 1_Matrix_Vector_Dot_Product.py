# Write a Python function that computes the dot product of a matrix and a vector. The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector.
# For example, an n x m matrix requires a vector of length m.

def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    # Check if number of columns in matrix == length of vector
    if len(a[0]) != len(b):
        return -1

    result = []
    for row in a:
        dot = sum(row[j] * b[j] for j in range(len(b)))
        result.append(dot)

    return result

print(matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]))