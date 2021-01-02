import cv2
import numpy as np
import os
from os.path import isfile, join

import sys
sys.path.insert(1, "/Users/binyugao/@github/ai")


def main():
    videoFolder = "./videos/"
    files = [f for f in os.listdir(imgFolder) if excludeFile(f)]
    files.sort()
    # print(files)
    
    for f in files:
        filename = imgFolder + f

        # Reading each file
        img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

        # Discard alpha channel
        img = img[:,:,:3]

        # Normalize image to 720P, empty space filled with black color
        img = resize_image_720P(img)

        # Save resized image to media folder 
        cv2.imwrite("/Users/binyugao/@github/ai/media/" + f, img)

main()
