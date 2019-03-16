#!/usr/bin/env python3

import numpy as np
import time
import os


def num_neighbors(grid, pos):
    neighbors = 0
    x,y = pos

    neighbors += grid[x-1][y-1] # Top Left
    neighbors += grid[x-1][y]   # Top
    neighbors += grid[x-1][y+1] # Top Right

    neighbors += grid[x][y-1]   # Left
    neighbors += grid[x][y+1]   # Right

    neighbors += grid[x+1][y-1] # Bottom Left
    neighbors += grid[x+1][y]   # Bottom
    neighbors += grid[x+1][y+1] # Bottom Right
                
    return neighbors


def update_state(grid):
    h, w = len(grid)-1, len(grid[0])-1
    new_grid = np.zeros(shape=(h+1,w+1))

    for x in range(h):
        for y in range(w):
            n = num_neighbors(grid, [x,y])
            cell = grid[x][y]
            if cell == 0 and n == 3:
                new_grid[x][y] = 1
            elif cell == 1 and n < 2:
                new_grid[x][y] = 0
            elif cell == 1 and 1 < n < 4:
                new_grid[x][y] = 1
            elif cell == 1 and n > 3:
                new_grid[x][y] = 0

    return new_grid


def print_grid(grid):
    for row in grid:
        for col in row:
            if col == 1:
                print("⬛️", end='')
            else:
                print("  ", end='')
        print()


def main():
    width = 80
    height = 60
    grid = np.random.randint(2, size=(height, width)) 

    while True:
        os.system('clear')
        print_grid(grid)
        grid = update_state(grid)
        time.sleep(.05)
       

if __name__ == "__main__":
    main()
