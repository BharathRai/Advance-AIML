# Program to print a simple grid with numbers

# 1. Define the grid using numbers. 0 represents an empty cell, 1 represents a filled cell.
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1]
]

# 2. The outer loop iterates through each row in the grid.
for row in grid:
    # 3. The inner loop iterates through each number (cell) in the current row.
    for cell in row:
        # 4. Print the number, followed by a space instead of a newline.
        print(cell, end=' ')
    
    # 5. After printing all numbers in a row, print a newline to move to the next line.
    print()