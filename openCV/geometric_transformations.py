import cv2
import numpy as np


""" reading file and plot it """
img = cv2.imread('images/google.jpg')  # cv2.IMREAD_GRAYSCALE
cv2.imshow('input image', img)
cv2.waitKey()

""" save image to file """
cv2.imwrite('images/save.jpg', img)
