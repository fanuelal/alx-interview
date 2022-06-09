#!/usr/bin/python3


def island_perimeter(grid):
    """that returns the perimeter of the island
    described in grid"""
    row = len(grid)
    col = len(grid[0])
    assert (1 <= row and col <= 100), "length must be between 1 an 100"


    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            assert (grid[i][j] == 0) or (grid[i][j] == 1),\
                                        "grid numbers must be 0 or 1"

            count = 0
            if grid[i][j] == 1:
                if j != (len(grid[i])-1):
                    if grid[i][j+1] == 0:
                        count += 1
                if j != 0:
                    if grid[i][j-1] == 0:
                        count += 1
                if i != (len(grid) - 1):
                    if grid[i+1][j] == 0:
                        count += 1
                if i != 0:
                    if grid[i-1][j] == 0:
                        count += 1

                perimeter += count

    return perimeter
