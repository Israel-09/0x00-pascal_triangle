#!/usr/bin/env python3
"""
matrix manipulation
"""


def rotate_2d_matrix(matrix):
    """rotates a square matrix 90 degrees clockwise
    Agrs:
        matrix (list): 2d matrix
    """
    N = len(matrix)

    for x in range(int(N / 2)):
        for y in range(x, N - x - 1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[N - 1 - y][x]
            matrix[N - y - 1][x] = matrix[N - x - 1][N - y - 1]
            matrix[N - x - 1][N - y - 1] = matrix[y][N - 1 - x]
            matrix[y][N - 1 - x] = temp


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
