import sys
sys.path.insert(1, "/Users/binyugao/@github/img2video")

import cv2
import numpy as np
import os
from os.path import isfile, join
import math

# Self
from resizeImg import resize_image_720P

# Consts
RES_720P = (1280, 720)
pathIn= "./images/"

imgName = "a1.jpg"

# Read img
img = cv2.imread(pathIn + imgName, cv2.IMREAD_UNCHANGED)

# Normalize image to 720P, empty space filled with black color
img = resize_image_720P(img)
