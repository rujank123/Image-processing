import cv2
import numpy as np

img = cv2.imread('brain.jpg')
median = cv2.medianBlur(img, 5)
compare = np.concatenate((img, median), axis=1) #side by side comparison

cv2.imshow('img', compare)
cv2.waitKey(0)
cv2.destroyAllWindows
median = cv2.medianBlur(img, 5)
gauss = cv2.GaussianBlur(img, (5,5), 0)

images = np.concatenate((median, gauss), axis=1)

cv2.imshow('img', images)