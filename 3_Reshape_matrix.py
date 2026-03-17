
import numpy as np

def reshape_matrix(a, new_shape):

    # Step 1: Flatten matrix
    flat = []
    for row in a:
        for val in row:
            flat.append(val)

    # Step 2: Check if reshape possible
    total_elements = len(flat)
    if total_elements != new_shape[0] * new_shape[1]:
        return []

    # Step 3: Build new matrix
    result = []
    index = 0

    for i in range(new_shape[0]):
        new_row = []
        for j in range(new_shape[1]):
            new_row.append(flat[index])
            index += 1
        result.append(new_row)

    return result