from getSoln import soln
from obtainGrid import obtain_grid
import numpy as np
import cv2 
import sys

image_name = input("Enter image name")
path = 'Sample Images/{}.png'.format(image_name)
name = path[-5:]
grid, solved_grid = soln(path)
img = obtain_grid(path)
original = img.copy()


array = np.array(img)
width = array.shape[1] // 9.0
height = array.shape[0] // 9.0


hi = []
np_grid = np.array(list(grid))
np_grid = np_grid.reshape((9, 9))
np_solved = np.array(list(solved_grid))
np_solved = np_solved.reshape((9, 9))

for i in range (0, 9):
    for j in range (0, 9):
        if np_grid[i][j] == str(0):
            cv2.putText(img, np_solved[i][j], (int((j) * width + width/10), int((i + 1) * height - height/10)), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 2 )

cv2.imwrite('Solved/{}'.format(name), img)
cv2.imshow('original', original)
cv2.waitKey(5000)
cv2.imshow('solved', img)
cv2.waitKey(0)