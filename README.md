# Sudoku-CNN
Sudoku solver using CNN

The main aim of the project is to create a **Convolution Neural Network** from scratch to detect and recognise digits in Sudoku grid. 
The recognised digits are then passed to sudoku solving algorithm published by Norvig. The solution is then mapped back into the grid.
The project is done in python language.

---

The accuracy of the CNN model used to detect digits is ~98%. Hence in some cases of misclassification of digits, we may not obtain the solution

---
## Libraries used
- OpenCV
- Tensorflow
- Numpy
---

## Work Flow

**OpenCV** was used to locate sudoku block. Various transformations are applied with OpenCV to obtain the sudoku block properly.

Original image: <br>
<img src = "process/0orig.jpg" width = 300px style = "padding:20px;"></img>

After obtaining the largest contour: <br>
<img src = "process/1big contour.png" width = 300px style = "padding:20px;"></img>

Obatining the border: <br>
<img src = "process/2contourbalck.png" width = 300px style = "padding:20px;"></img>

From the border, we transform perspective and get warped image: <br>
<img src = "process/5warped.png" width = 300px style = "padding:20px;"></img>

Adaptive thresholding is applied to get proper input: <br>
<img src = "process/6thresh.png" width = 300px style = "padding:20px;"></img>

The output obtained is divided into 81 equal squares.
Each square is the fed into the **CNN model** created with custom data to predict digit in the square.
The deep learning model predicts and produces predictions as a string which are fed into the sudoku solving algorithm.
The sudoku solving algorithm produces the solution as string. 
The solution string is then mapped into the image with the help of **OpenCV** and **Numpy**.

---
## Usage
'python3 Sudoku.py'
The program asks for input image name. It has some sample images which can be used for prediction, their names being 1 to 6 repectively.
Hence giving a number between 1-6 gives solution for one of the image.

---





