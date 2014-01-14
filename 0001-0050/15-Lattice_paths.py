"""
Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

r,r,b,b
r,b,r,b
r,b,b,r
b,r,r,b
b,r,b,r
b,b,r,r

How many such routes are there through a 20 x 20 grid?
"""

current_positions = {(0, 0): 1}
gridSize = 20

while (gridSize, gridSize) not in current_positions:
    new_positions = {}
    for (x, y) in current_positions:
        v = current_positions[(x, y)]

        if x < gridSize:
            p = (x + 1, y)
            if p not in new_positions:
                new_positions[p] = v
            else:
                new_positions[p] += v

        if y < gridSize:
            p = (x, y + 1)
            if p not in new_positions:
                new_positions[p] = v
            else:
                new_positions[p] += v
    current_positions = new_positions

print new_positions[(gridSize, gridSize)]