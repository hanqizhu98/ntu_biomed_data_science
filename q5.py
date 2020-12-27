import numpy as np
import random
import sys

grid = []

# # the size of grid
# x = 5
# y = 5

# # the number of color
# red = 12
# blue = 13

# count = 0

# for i in range(y):
#     for j in range(x):
#         if (count >= red):   
#             grid.append(1)
#         else:
#             grid.append(0)
#         count += 1

# the size of grid
x = 64
y = 64

# the number of color
red = 139
blue = 1451
green = 977
white = 1072
yellow = 457

count = 0

for i in range(y):
    for j in range(x):
        if (count >= red):   
            grid.append(1)
        elif (count >= red+blue):   
            grid.append(2)
        elif (count >= red+blue+green):   
            grid.append(3)
        elif (count >= red+blue+green+white):   
            grid.append(4)
        else:
            grid.append(0)
        count += 1


smallest_config = []
smallest_penalty = sys.maxsize
for m in range(100000000):
    random.shuffle(grid)

    # convert the array to a vector
    mat = np.array(grid)

    # reshape the vector to a 2d matrix (2d array)
    mat = mat.reshape(x,y)
    
    penalty = 0
    for i in range(y):
        for j in range(x):
            if (j < x-1):
                if (mat[i][j] == mat[i][j+1]):
                    penalty += 1
            if (i < y-1):
                if (mat[i][j] == mat[i+1][j]):
                    penalty += 1
    
    if (penalty < smallest_penalty):
        smallest_penalty = penalty
        smallest_config = mat

        if (smallest_penalty == 0):
            break
print("the smallest penalty is", smallest_penalty)
print(smallest_config)


                

