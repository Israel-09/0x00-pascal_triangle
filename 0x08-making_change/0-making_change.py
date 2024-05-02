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

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1


print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))
