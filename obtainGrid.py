import cv2
import numpy as np

#path = '/Users/sudheeradh/sudoku_fail/fail/3.png'
def obtain_grid(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (500, 500))
    original = img.copy()
    original = cv2.resize(original, (500, 500))
    ##### Applying image transformations to get outline

    morph = img.copy()

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)
    morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)


    # split the morph image into channels
    image_channels = np.split(np.asarray(morph), 3, axis=2)

    channel_height, channel_width, _ = image_channels[0].shape

    # apply Otsu threshold to each channel
    for i in range(0, 3):
        _, image_channels[i] = cv2.threshold(~image_channels[i], 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
        image_channels[i] = np.reshape(image_channels[i], newshape=(channel_height, channel_width, 1))

    # merge the channels
    image_channels = np.concatenate((image_channels[0], image_channels[1], image_channels[2]), axis=2)

    image_channels = cv2.cvtColor(image_channels, cv2.COLOR_BGR2GRAY)

    ### End of applying transformations

    ### Obtaining contours and Cutting out the outline

    contours, h = cv2.findContours(image_channels, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    blank = np.zeros(original.shape)

    cntsSorted = sorted(contours, key=lambda x: cv2.contourArea(x))
    cut = cntsSorted[-1]
    x, y, w, h = cv2.boundingRect(cut)

    image = original[y:y + h, x:x + w]

    ### End of Obtaining contours and Cutting out the outline


    ### Straightening of cut image

    org_crop = image.copy()
    return org_crop

'''
foto = getim(path)
foto = cv2.resize(foto, (500, 500))
cv2.imshow('hi', foto)
cv2.waitKey(0)
'''
