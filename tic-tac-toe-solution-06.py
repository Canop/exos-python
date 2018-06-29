#!/usr/bin/env python3
# This proposal for a solution is purposefully not using classes
# It has been designed to work whatever the grid size (which wasn't a requirement)
# Note that it has been written by a Python noob

from random import randint

def create_grid(size=3):
    return [ [' ']*size for i in range(size) ]

# build a pretty string representation of the grid state
# work for any dimension of the grid
def grid_to_string(grid):
    sep = "+---"*len(grid) + "+"
    mask = "| {} "*len(grid) + "|"
    lines = [sep]
    for row in grid:
        lines.append(mask.format(*row))
        lines.append(sep)
    return "\n".join(lines)

def set_cell(grid, val, x, y):
    grid[x][y] = val

def random_pos(size=3):
    return (randint(0, size-1), randint(0, size-1))

def user_pos(invite="Type a position"):
    str = input(invite+":\n").strip()
    return tuple([ int(x) for x in str.split(" ") ])

def is_valid(grid, x, y):
    return (0 <= x <= len(grid)) and (0 <= y <= len(grid)) and (grid[x][y]==" ")

# ask the player for a position and returns it
# ask again until the position is valid
def make_play(grid, val, ask):
    while True:
        pos = ask()
        if is_valid(grid, *pos):
            set_cell(grid, val, *pos)
            return pos
        print("invalid position")

def main():
    size = int(input("Please give the grid size:\n"))
    grid = create_grid(size)
    players = [
            {'name':'X', 'play':lambda:random_pos(size)},
            {'name':'O', 'play':user_pos}
    ]
    next_player_index = 0
    while True:
        player = players[next_player_index]
        make_play(grid, player['name'], player['play'])
        print(grid_to_string(grid))
        next_player_index = (next_player_index+1)%len(players)

main()

