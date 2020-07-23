# Sudoku-CNN
Sudoku solver using CNN

The main aim of the project is to create a Convolution Neural Network from scratch to detect and recognise digits in Sudoku grid. 
The recognised digits are then passed to sudoku solving algorithm published by Norvig. The solution is then mapped back into the grid.
The project is done in python language

---
## Libraries used
- OpenCV
- Tensorflow
- Numpy
---

## Work Flow

OpenCV was used to locate sudoku block. Various transformations are applied to obtain the sudoku block properly.

Original image:
<img src = "process/0orig.jpg" width = 300px style = "padding:20px;"></img>

After obtaining the largest contour:
<img src = "process/1big contour.png" width = 300px style = "padding:20px;"></img>

Obatining the border:
<img src = "process/2contourbalck.png" width = 300px style = "padding:20px;"></img>

From the border, we transform perspective and get warped image:
<img src = "process/5warped.png" width = 300px style = "padding:20px;"></img>

Adaptive thresholding is applied to get proper input:
<img src = "process/6thresh.png" width = 300px style = "padding:20px;"></img>





