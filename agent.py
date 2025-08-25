import time
from collections import deque
import os

# 5x5 grid
# 0 = empty, 1 = wall, 2 = food
grid = [
    [0, 2, 0, 1, 1],
    [1, 1, 0, 2, 0],
    [0, 0, 0, 0, 0],
    [2, 2, 1, 0, 2],
    [0, 0, 0, 0, 0]
]

agent_pos = [0, 0]  # start top-left


def perceive(pos):
    x, y = pos
    return grid[y][x]


def clean(pos):
    x, y = pos
    if grid[y][x] == 2:
        grid[y][x] = 0


def neighbors(pos):
    x, y = pos
    moves = []
    if x + 1 < len(grid[0]) and grid[y][x + 1] != 1:  # right
        moves.append([x + 1, y])
    if x - 1 >= 0 and grid[y][x - 1] != 1:  # left
        moves.append([x - 1, y])
    if y + 1 < len(grid) and grid[y + 1][x] != 1:  # down
        moves.append([x, y + 1])
    if y - 1 >= 0 and grid[y - 1][x] != 1:  # up
        moves.append([x, y - 1])
    return moves


def bfs(start):
    """Find nearest food using BFS"""
    q = deque([(start, [])])
    visited = set()
    while q:
        (x, y), path = q.popleft()
        if grid[y][x] == 2:  # found food
            return path
        for nx, ny in neighbors([x, y]):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append(([nx, ny], path + [[nx, ny]]))
    return []  # no food left


def display_grid(grid, agent_pos, step):
    os.system('cls' if os.name == 'nt' else 'clear')  # clear screen for animation
    print(f"Step {step}")
    print("+" + "---+" * len(grid[0]))
    for y in range(len(grid)):
        row = "|"
        for x in range(len(grid[0])):
            if [x, y] == agent_pos:
                row += " P |"   # Pac-Man
            elif grid[y][x] == 1:
                row += " # |"   # Wall
            elif grid[y][x] == 2:
                row += " F |"   # Food
            else:
                row += " - |"   # Empty
        print(row)
        print("+" + "---+" * len(grid[0]))


for step in range(1, 50):  # run max 50 steps
    if perceive(agent_pos) == 2:
        clean(agent_pos)

    display_grid(grid, agent_pos, step)

    path = bfs(agent_pos)  # get shortest path to nearest food
    if not path:
        print("🎉 All food eaten! Pac-Man wins!")
        break

    # move one step along path
    agent_pos = path[0]

    time.sleep(2)
