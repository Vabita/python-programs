def sum_diagonal_elements(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols:
        return None

    diagonal_sum = 0
    for i in range(rows):
        diagonal_sum += matrix[i][i]

    return diagonal_sum


m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

m2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

diagonal_sum_3x3 = sum_diagonal_elements(m1)
if diagonal_sum_3x3 is not None:
    print("Sum of diagonal elements in the 3x3 array:", diagonal_sum_3x3)
else:
    print("The matrix is not square.")

diagonal_sum_4x4 = sum_diagonal_elements(m2)
if diagonal_sum_4x4 is not None:
     print("Sum of diagonal elements in the 4x4 array:", diagonal_sum_4x4)
else:
    print("The matrix is not square.")

