#!/usr/bin/python3
"""
pascal triangle algorithm
"""

def pascal_triangle(n):
    """
    pascal triangle generator
    """
    
    if type(n) is not int or n < 0:
        raise TypeError("n must be an integer not less than 0")

    triangle = [[1]]

    for i in range(1, n + 1):
        row = [1]
        for k in range(1, i):
            value = triangle[i - 1][k] + triangle[i - 1][k - 1]
            row.append(value)
        row.append(1)
        triangle.append(row)

    return triangle
