from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import cv2
import numpy as np

model = load_model('model/digit_recog_su.h5')


def predict(img):
	img = cv2.resize(img, (28, 28))
	img = np.atleast_3d(img)
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	classes = model.predict(x)
	return np.argmax(classes)



'''
path ='models/2.png'
img = image.load_img(path, target_size=(28, 28), grayscale = True)
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

classes = model.predict(x)

print(classes)
print(np.argmax(classes))
'''