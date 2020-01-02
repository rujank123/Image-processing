# import cv2
# img = cv2.imread('brain.jpg', 0)
# cv2.imshow('Greyscale', img)
# blur = cv2.blur(img,(5,5))
# cv2.imshow('mean filtr processing', blur)
# cv2.waitKey(0)

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("")
gauss_mask = cv2.GaussianBlur(image, (9, 9), 10.0)
image_sharp = cv2.addWeighted(image, 2, gauss_mask, -1, 0)
cv2.imshow("Sharpen_RUJAN", image_sharp)
kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])
# '''kernel = np.array([[-1, -1, -1, -1, -1],
#                    [-1,  1,  2,  1, -1],
#                    [-1,  2,  4,  2, -1],
#                    [-1,  1,  2,  1, -1],
#                    [-1, -1, -1, -1, -1]])'''

image_hpf = cv2.filter2D(image, -1, kernel)
cv2.imshow("High Pass Filter_RUJAN", image_hpf)
cv2.waitKey(0)