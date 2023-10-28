def split_matrix(matrix):
    n = len(matrix)
    n2 = n // 2
    A11 = [row[:n2] for row in matrix[:n2]]
    A12 = [row[n2:] for row in matrix[:n2]]
    A21 = [row[:n2] for row in matrix[n2:]]
    A22 = [row[n2:] for row in matrix[n2:]]
    return A11, A12, A21, A22

def add_matrices(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]
    return result

def subtract_matrices(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] - B[i][j]
    return result

def strassen_matrix_multiply(A, B):
    if len(A) == 1:
        # Base case: Standard matrix multiplication for 1x1 matrices
        return [[A[0][0] * B[0][0]]]

    n = len(A)
    n2 = n // 2

    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    # Recursive calls
    P1 = strassen_matrix_multiply(A11, subtract_matrices(B12, B22))
    P2 = strassen_matrix_multiply(add_matrices(A11, A12), B22)
    P3 = strassen_matrix_multiply(add_matrices(A21, A22), B11)
    P4 = strassen_matrix_multiply(A22, subtract_matrices(B21, B11))
    P5 = strassen_matrix_multiply(add_matrices(A11, A22), add_matrices(B11, B22))
    P6 = strassen_matrix_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22))
    P7 = strassen_matrix_multiply(subtract_matrices(A11, A21), add_matrices(B11, B12))

    # Calculate C11, C12, C21, C22
    C11 = add_matrices(subtract_matrices(add_matrices(P5, P4), P2), P6)
    C12 = add_matrices(P1, P2)
    C21 = add_matrices(P3, P4)
    C22 = subtract_matrices(subtract_matrices(add_matrices(P5, P1), P3), P7)

    # Combine the four resulting submatrices to obtain the final result
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n2):
        for j in range(n2):
            result[i][j] = C11[i][j]
            result[i][j + n2] = C12[i][j]
            result[i + n2][j] = C21[i][j]
            result[i + n2][j + n2] = C22[i][j]

    return result

# Example usage:
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = strassen_matrix_multiply(A, B)
for row in result:
    print(row)
