#!/usr/bin/python3
"""
    solution to island perimeter problem
"""


def find_exposed_sides(pos, grid):
    """_summary_

    Args:
        grid (_type_): _description_
        col (_type_): _description_
    """
    x, y = pos
    grid_height = len(grid) - 1
    grid_width = len(grid[0]) - 1

    top = grid[x - 1][y] if x > 0 else 0
    right = grid[x][y - 1] if y > 0 else 0
    bottom = grid[x + 1][y] if x < grid_height else 0
    left = grid[x][y + 1] if y < grid_width else 0

    exp_sides = 4 - top - right - bottom - left
    return exp_sides


def island_perimeter(grid):
    """calcalate the perimeter of the island

    Args:
        grid (2d array): grid map
    """
    if not grid:
        return 0

    grid_height = len(grid)
    grid_width = len(grid[0])
    perimeter = 0
    island = 0

    if grid_height > 100 or grid_width > 100:
        return 0

    for i in range(grid_height):
        for j in range(grid_width):
            if grid[i][j] == 1:
                exp_sides = find_exposed_sides((i, j), grid)
                if island == 1 and exp_sides > 0:
                    return 0
                if exp_sides == 4:
                    island += 1
                perimeter += exp_sides
    return perimeter
