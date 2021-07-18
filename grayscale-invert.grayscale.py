import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('infile.jpg')    
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def rgb2gray(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plt.imshow(gray, cmap= 'gray')
    plt.show()                                                              

rgb2gray(image)    # Displays the grayscale image.

def inverte(image):
    image = (255-image)    
    plt.imshow(image)
    plt.show()

inverte(image)       # Displays the invert of grayscale image.
