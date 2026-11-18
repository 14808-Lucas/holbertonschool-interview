#!/usr/bin/python3
"""Defines makeChange, the fewest coins needed to meet a total."""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total.

    coins is a list of coin values, each available in unlimited supply.
    Returns 0 if total is 0 or less, and -1 if total cannot be met.
    """
    if total <= 0:
        return 0
    infinity = total + 1
    fewest = [0] + [infinity] * total
    for coin in set(coins):
        for amount in range(coin, total + 1):
            if fewest[amount - coin] + 1 < fewest[amount]:
                fewest[amount] = fewest[amount - coin] + 1
    if fewest[total] == infinity:
        return -1
    return fewest[total]
