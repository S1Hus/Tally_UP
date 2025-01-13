import random

values = {0,1,2,3,"-","*"}
grid = []
i = 0

while i < 16:
    grid.append(random.choice(list(values)))
    i+=1

print(grid)
