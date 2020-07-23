from obtainGrid import obtain_grid
import cv2
import numpy as np
import os
#from cnn_pred import predict

from PIL import Image


path = '/Users/sudheeradh/Sudoku_project/sad/yo/25.jpg'
img = obtain_grid(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

array = np.array(img)
width = array.shape[1] // 9.0
height = array.shape[0] // 9.0

di = 21
os.mkdir("/Users/sudheeradh/Sudoku_project/data/{}".format(di))

for i in range (0, 9):
	for j in range (0, 9):
		cell = array[i*int(height):(i+1)*int(height), j*int(width) :(j + 1)*int(width)]
		im = Image.fromarray(cell)
		
		im.save("data/{}/{}_{}_{}.jpg".format(di,i,j,di))


#print(predict(cv2.resize(cell, (28, 28))))

#print(cell.shape)

cv2.imshow('window', img)
cv2.waitKey(0)