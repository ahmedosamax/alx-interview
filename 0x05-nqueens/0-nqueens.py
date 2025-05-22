#!/usr/bin/python3
"""
Solves the N Queens puzzle using backtracking.
Usage: nqueens N
Only the sys module is allowed.
"""

import sys


def is_safe(solution, row, col):
    """Check if placing a queen at (row, col) is safe with current solution."""
    for prev_col in range(col):
        prev_row = solution[prev_col]
        if prev_row == row or \
           abs(prev_row - row) == abs(prev_col - col):
            return False
    return True


def solve_nqueens(n, col=0, solution=[]):
    """Recursively solve the N Queens problem and print solutions."""
    if col == n:
        print([[i, solution[i]] for i in range(n)])
        return

    for row in range(n):
        if is_safe(solution, row, col):
            solve_nqueens(n, col + 1, solution + [row])


def validate_args():
    """Validate command line arguments and return board size."""
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
    return n


if __name__ == "__main__":
    N = validate_args()
    solve_nqueens(N)
