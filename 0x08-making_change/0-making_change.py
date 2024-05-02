#!/usr/bin/python3
"""
    compute least number of coin[s]
    needed to make change for a given amount
"""


def makeChange(coins, total, memo={}):
    """_summary_

    Args:
        coins (_type_): _description_
        total (_type_): _description_
    """
    if total in memo:
        return memo[total]
    if total == 0:
        return 0
    if total < 0:
        return -1

    best_count = -1

    for coin in coins:
        remainder = total - coin
        remainder_change = 1 + makeChange(coins, remainder, memo)
        if remainder_change > 0:
            if best_count == -1 or remainder_change < best_count:
                best_count = remainder_change
    memo[total] = best_count
    return best_count
