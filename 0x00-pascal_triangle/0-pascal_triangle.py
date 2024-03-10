#!/usr/bin/python3
"""
pascal triangle algorithm
"""


def get_next_row(prev):
    """
    helper function to generate next row
    """
    row = [1]
    for i in range(1, len(prev)):
        row.append(prev[i] + prev[i - 1])
    row.append(1)
    return row


def pascal_triangle(n):
    """
    pascal triangle generator
    """

    if type(n) is not int or n < 0:
        raise TypeError("n must be an integer not less than 0")

    triangle = []
    row = [1]
    for i in range(n):
        triangle.append(row)
        row = get_next_row(row)

    return triangle
