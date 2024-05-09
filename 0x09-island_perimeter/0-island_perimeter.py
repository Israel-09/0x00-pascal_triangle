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
    try:
        top = grid[x - 1][y]
        right = grid[x][y - 1]
        bottom = grid[x - 1][y]
        left = grid[x][y + 1]
    except:
        return 0
    exp_sides = 4 - top - right - bottom - left
    return exp_sides


def island_perimeter(grid):
    """calcalate the perimeter of the island

    Args:
        grid (2d array): grid map
    """
    if not grid:
        return
    
    grid_height = len(grid)
    grid_width = len(grid[0])
    perimeter = 0

    if grid_height > 100 or grid_width > 100:
        return
    
    for i in range(grid_height):
        for j in range(grid_width):
            if grid[i][j] == 1:
                exp_sides = find_exposed_sides((i, j), grid)
                perimeter += exp_sides
    return perimeter
                
  
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))