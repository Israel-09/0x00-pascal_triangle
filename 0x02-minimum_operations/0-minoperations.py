#!/usr/bin/python3
"""
min operations algorithm
"""


def minOperations(n):
    """
    solution
    """
    if n < 2:
        return 0

    for i in range(2, n + 1):
        if n % i == 0:
            return i + minOperations(int(n/i))
