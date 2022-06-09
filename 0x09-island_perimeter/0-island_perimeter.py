#!/usr/bin/python3
""" Module Perimeter  """


def test0(n):
    """
    return 0 or 1
    """
    if (n == 0):
        return 1
    return 0


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    row = len(grid)
    col = len(grid[0])
    assert (1 <= row and col <= 100), "length must be between 1 an 100"

    p = 0
    for i in range(row):
        for j in range(col):
            assert (grid[i][j] == 0) or (grid[i][j] == 1),\
                                        "grid numbers must be 0 or 1"
            if grid[i][j] == 1:
                if i-1 < 0:
                    p += 1
                else:
                    p += test0(grid[i-1][j])
                if j-1 < 0:
                    p += 1
                else:
                    p += test0(grid[i][j-1])

                try:
                    p += test0(grid[i+1][j])
                except IndexError:
                    p += 1
                try:
                    p += test0(grid[i][j+1])
                except IndexError:
                    p += 1

    return p
