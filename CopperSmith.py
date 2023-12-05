##
def coppersmith_winograd_matrix_multiply(A, B):
    n = len(A)

    # Base case: standard matrix multiplication for small matrices
    if n <= 2:
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += A[i][k] * B[k][j]
        return result

    # Split matrices into submatrices
    n2 = n // 2
    A11 = [row[:n2] for row in A[:n2]]
    A12 = [row[n2:] for row in A[:n2]]
    A21 = [row[:n2] for row in A[n2:]]
    A22 = [row[n2:] for row in A[n2:]]
    B11 = [row[:n2] for row in B[:n2]]
    B12 = [row[n2:] for row in B[:n2]]
    B21 = [row[:n2] for row in B[n2:]]
    B22 = [row[n2:] for row in B[n2:]]

    # Recursive calls for intermediate products
    M1 = coppersmith_winograd_matrix_multiply(add_matrices(A11, A22), add_matrices(B11, B22))
    M2 = coppersmith_winograd_matrix_multiply(add_matrices(A21, A22), B11)
    M3 = coppersmith_winograd_matrix_multiply(A11, subtract_matrices(B12, B22))
    M4 = coppersmith_winograd_matrix_multiply(A22, subtract_matrices(B21, B11))
    M5 = coppersmith_winograd_matrix_multiply(add_matrices(A11, A12), B22)
    M6 = coppersmith_winograd_matrix_multiply(subtract_matrices(A21, A11), add_matrices(B11, B12))
    M7 = coppersmith_winograd_matrix_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22))

    # Calculate result matrices
    C11 = subtract_matrices(add_matrices(add_matrices(M1, M4), M7), M5)
    C12 = add_matrices(M3, M5)
    C21 = add_matrices(M2, M4)
    C22 = subtract_matrices(subtract_matrices(add_matrices(M1, M3), M2), M6)

    # Combine submatrices to obtain the final result
    result = [[0] * n for _ in range(n)]
    for i in range(n2):
        for j in range(n2):
            result[i][j] = C11[i][j]
            result[i][j + n2] = C12[i][j]
            result[i + n2][j] = C21[i][j]
            result[i + n2][j + n2] = C22[i][j]

    return result

def add_matrices(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]
    return result

def subtract_matrices(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] - B[i][j]
    return result
