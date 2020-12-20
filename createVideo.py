import sys
sys.path.insert(1, "/Users/binyugao/@github/img2video")

import cv2
import numpy as np
import glob
import os
from os.path import isfile, join

# Self
from resizeImg import resize_image_720P

# Consts
RES_720P = (1280, 720)

# Vars
pathIn= "./images/"
pathOut = "video.avi"
frame_array = []
# frames = [1, 1, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
frames = [51, 58, 10, 70, 51, 13, 25, 77, 13, 115, 25, 25, 25, 25]

files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

for i in range(len(files)):
    filename=pathIn + files[i]

    # Reading each file
    img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

    # Normalize image to 720P, empty space filled with black color
    img = resize_image_720P(img)

    # Inserting the frames into an image array
    for j in range(frames[i]):
        frame_array.append(img)


out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), 25, RES_720P)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])

out.release()
