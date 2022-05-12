#!/usr/bin/python3
"""Module N-queens"""
import sys


def nqueens(num: int):
    """
    will do the backtracking
    """
    mat = [[0 for x in range(num)] for y in range(num)]
    print(str(mat))


if __name__ == "__main__":
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    nqueens(int(sys.argv[1]))
