#!/usr/bin/python3
"""_summary_
"""


def sieve(n):
    """_summary_

    Args:
        n (int): _description_
    """
    prime = [True for i in range(n + 1)]
    p = 2

    while p * p < n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return [p for p in range(2, n + 1) if prime[p]]


def isWinner(x, nums):
    """_summary_

    Args:
        x (int): _description_
        nums (list): _description_
    """
    maria = 0
    ben = 0

    for i in range(x):
        primes = len(sieve(nums[i]))
        if primes > 0:
            if primes & 2 == 0:
                ben += 1
            else:
                maria += 1
    if maria == ben:
        return None
    return "Ben" if ben > maria else "Maria"

print("Winner: {}".format(isWinner(0, [1, 1, 0, 0, 1, 8])))
