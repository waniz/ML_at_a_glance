import cv2
import numpy as np


""" reading file and plot it """
img = cv2.imread('images/google.jpg')  # cv2.IMREAD_GRAYSCALE
cv2.imshow('input image', img)
cv2.waitKey()

""" save image to file """
cv2.imwrite('images/save.jpg', img)

""" split image to channels """
g, b, r = cv2.split(img)
gbr_img = cv2.merge((g, b, r))
rbr_img = cv2.merge((r, b, r))
cv2.imshow('Original', img)
cv2.imshow('GRB', gbr_img)
cv2.imshow('RBR', rbr_img)
cv2.waitKey()
