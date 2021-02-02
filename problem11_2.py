
import pandas as pd
import numpy as np

grid = pd.read_csv('assets/P11.csv', header=None)

grid = grid.to_numpy()

def largest_hor(grid):
    largests = []
    largest_product = 0
    for array in grid:
        index1, index2 = 0, 4
        while index2 <= len(array):
            product = 1
            for value in array[index1:index2]:
                product*=value
            if product > largest_product:
                largest_product = product
            index1+=1
            index2+=1
    return largest_product

def largest_ver(grid):
    return largest_hor(grid.transpose())

def largest_dia(grid):
    diag = np.diag_indices(4)
    row1,row2 = 0,4
    largest_product = 0
    while row2 <= 20:
        col1, col2 = 0, 4
        while col2 <= 20:
            tempGrid = grid[row1:row2, col1:col2]
            tempArray = tempGrid[diag]
            product = 1
            for value in tempArray:
                product *= value
            if product > largest_product:
                largest_product = product
            col1 += 1
            col2 += 1
        row1+=1
        row2+=1
    return largest_product

print("largest overall: ", max(largest_hor(grid), largest_ver(grid), largest_dia(grid), largest_dia(np.fliplr(grid))))
