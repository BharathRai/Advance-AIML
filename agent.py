grid = [
    [0, 2, 0],
    [1, 0, 2],
    [0, 0, 0]
]

agent_pos = [0, 0]  # start top-left


def perceive(pos):
    x, y = pos
    return grid[y][x]


def clean(pos):
    x, y = pos
    if grid[y][x] == 2:
        grid[y][x] = 0
        print(f"Cleaned cell at {pos}")


def move(pos, direction):
    x, y = pos
    if direction == 'right':
        if x + 1 < len(grid[0]) and grid[y][x + 1] != 1:
            return [x + 1, y]
    elif direction == 'left':
        if x - 1 >= 0 and grid[y][x - 1] != 1:
            return [x - 1, y]
    elif direction == 'down':
        if y + 1 < len(grid) and grid[y + 1][x] != 1:
            return [x, y + 1]
    elif direction == 'up':
        if y - 1 >= 0 and grid[y - 1][x] != 1:
            return [x, y - 1]
    # invalid move or blocked
    print(f"Move {direction} blocked or invalid.")
    return pos


for _ in range(10):
    print(f"Agent at {agent_pos}")
    if perceive(agent_pos) == 2:
        clean(agent_pos)
    
    direction = input("Enter direction to move (up/down/left/right): ").strip().lower()
    new_pos = move(agent_pos, direction)
    if new_pos == agent_pos:
        print("Agent stays at the same position.")
    else:
        print(f"Moving from {agent_pos} to {new_pos}")
        agent_pos = new_pos
