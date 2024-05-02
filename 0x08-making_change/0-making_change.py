#!/usr/bin/python3
"""
    compute least number of coin[s]
    needed to make change for a given amount
"""


def makeChange(coins, total):
    """_summary_

    Args:
        coins (_type_): _description_
        total (_type_): _description_
    """

    if total <= 0:
        return 0
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        while total >= coin:
            change += total // coin
            total -= (total // coin) * coin
    return change if total == 0 else -1
