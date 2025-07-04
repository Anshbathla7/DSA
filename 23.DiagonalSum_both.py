def both_diagonals_sum(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]                  # Primary diagonal
        total += matrix[i][n - i - 1]          # Secondary diagonal

    # Subtract the middle element once if matrix has odd dimensions (it was added twice)
    if n % 2 == 1:
        total -= matrix[n // 2][n // 2]

    return total

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Sum of both diagonals:", both_diagonals_sum(matrix))
