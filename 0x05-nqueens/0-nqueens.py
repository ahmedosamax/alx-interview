#!/usr/bin/python3
"""
Solves the N Queens puzzle using backtracking.
Usage: nqueens N
- N must be an integer >= 4
- Only the sys module is allowed
- Prints all possible solutions: one solution per line
- Format: list of lists with [row, col] positions for each queen
"""

import sys


def print_board(board):
    """Prints the board configuration in the required format."""
    result = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                result.append([i, j])
    print(result)


def isSafe(board, row, col, n):
    """Checks if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col, n):
    """Uses backtracking to place queens on the board."""
    if col == n:
        print_board(board)
        return

    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            solveNQUtil(board, col + 1, n)
            board[i][col] = 0  # Backtrack


def validate(args):
    """Validates and parses command-line arguments."""
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(args[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


if __name__ == "__main__":
    N = validate(sys.argv)
    board = [[0] * N for _ in range(N)]
    solveNQUtil(board, 0, N)
