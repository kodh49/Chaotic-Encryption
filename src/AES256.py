import numpy as np  # Load numpy module
import cv2  # Load openCV module
from sympy import sieve  # Euler phi function

image = cv2.imread("img/img_01.jpg", cv2.COLOR_BGR2RGB)
dimensions = image.shape
# Height, Width, number of channels in image
height = dimensions[0]
width = dimensions[1]
channels = dimensions[2]
print("Dimension: ", height, width, channels)
print(image)
