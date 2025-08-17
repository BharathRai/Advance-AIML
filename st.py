# Program to find start (S) and task (T) cells in a grid

# The grid is like a map made of text
grid = [
    "################",
    "#S.............#",
    "#.####.T.#####.#",
    "#......#.......#",
    "#####.T.######.#",
    "#..............#",
    "################",
]

# A place to remember the start's location
start_location = None 
# An empty list to keep track of all the task locations we find
task_locations = []

# Go through each row of the map, from top to bottom
for row_number, row in enumerate(grid):
    # In each row, go through each character, from left to right
    for column_number, character in enumerate(row):
        
        # If the character is 'S'
        if character == 'S':
            # Remember its location
            start_location = (row_number, column_number)

        # If the character is 'T'
        elif character == 'T':
            # Add its location to our list of tasks
            task_locations.append((row_number, column_number))

# Show the final results
print(f"Start 'S' was found at: {start_location}")
print(f"Tasks 'T' were found at: {task_locations}")