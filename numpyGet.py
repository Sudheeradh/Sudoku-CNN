from obtainGrid import obtain_grid
import cv2
import numpy as np
import os
from cnn_pred import predict


def get_digits(path):
	img = obtain_grid(path)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	array = np.array(img)
	width = array.shape[1] // 9.0
	height = array.shape[0] // 9.0

	val = []
	struct = []

	for i in range (0, 9):
		for j in range (0, 9):
			cell = array[i*int(height):(i+1)*int(height), j*int(width) :(j + 1)*int(width)]
			val.append(predict(cell))

	grid = ''.join(str(e) for e in val)
	return grid

'''print(grid)
print(type(val))
print(type(grid))
'''