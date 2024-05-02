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

    if total < 0:
        return -1
    if total == 0:
        return 0

    memo = {}

    def helper(total):
        """_summary_

        Args:
            total (_type_): _description_

        Returns:
            _type_: _description_
        """
        if total in memo:
            return memo[total]
        if total == 0:
            return 0
        if total < 0:
            return float('inf')

        best_count = float('inf')

        for coin in coins:
            remainder = total - coin
            remainder_change = helper(remainder)
            if remainder_change != float('inf'):
                best_count = min(best_count, remainder_change + 1)

        memo[total] = best_count
        return best_count

    best_count = helper(total)
    return best_count if best_count != float('inf') else -1

