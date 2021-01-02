import cv2
import numpy as np
import os
from os.path import isfile, join

import sys
sys.path.insert(1, "/Users/binyugao/@github/ai")

mediaFolder = "./media"

# Resizes a image and maintains aspect ratio
def maintain_aspect_ratio_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # Grab the image size and initialize dimensions
    dim = None
    (h, w) = image.shape[:2]

    # Return original image if no need to resize
    if width is None and height is None:
        return image

    # We are resizing height if width is none
    if width is None:
        # Calculate the ratio of the height and construct the dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    # We are resizing width if height is none
    else:
        # Calculate the ratio of the width and construct the dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # Return the resized image
    return cv2.resize(image, dim, interpolation=inter)



# @input: image is cv2.imread obj
# @return: normalized cv2 image obj: f
def resize_image_720P(image):
    WIDTH = 1280
    HEIGHT = 720
    height, width = image.shape[:2]
    xFactor = WIDTH / width
    yFactor = HEIGHT / height

    if yFactor < xFactor: # 说明x方向上需要填充黑色, 按照y来resize
        image = maintain_aspect_ratio_resize(image, height=HEIGHT)
    else:
        image = maintain_aspect_ratio_resize(image, width=WIDTH)

    #Creating a dark square with NUMPY
    f = np.zeros((HEIGHT,WIDTH,3),np.uint8)

    #Getting the centering position
    ax,ay = (WIDTH - image.shape[1])//2,(HEIGHT - image.shape[0])//2

    #Pasting the 'image' in a centering position
    f[ay:image.shape[0]+ay,ax:ax+image.shape[1]] = image

    #Showing results (just in case)
    # cv2.imshow("IMG",f)
    #A pause, waiting for any press in keyboard
    # cv2.waitKey(0)

    return f


def excludeFile(f):
    return f[0] != '.' 


def main():
    imgFolder = "./images/"
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
