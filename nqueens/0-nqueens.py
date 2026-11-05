#!/usr/bin/python3
"""Solves the N queens puzzle and prints every solution.

Usage: nqueens N
"""
import sys


def solve(n, row, queens, cols, diag1, diag2):
    """Place queens row by row and print each full solution.

    queens holds [row, col] pair placed so far. cols, diag1 and diag2
    are sets of the columns and diagonals already under attack.
    """
    if row == n:
        print(queens)
        return
    for col in range(n):
        if col in cols or row - col in diag1 or row + col in diag2:
            continue
        queens.append([row, col])
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)
        solve(n, row + 1, queens, cols, diag1, diag2)
        queens.pop()
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)


def main():
    """Check the command-line argument, then print every solution."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(n, 0, [], set(), set(), set())


if __name__ == "__main__":
    main()