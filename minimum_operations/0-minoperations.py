#!/usr/bin/python3
"""Defines minOperations, the fewest Copy All and Paste steps to reach n H."""


def minOperations(n):
    """Return the fewest operations needed to get exactly n H characters.
    """
    if not isinstance(n, int) or n < 2:
        return 0
    operations = 0
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    if n > 1:
        operations += n
    return operations
