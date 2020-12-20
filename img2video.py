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
pathOut = "/Users/binyugao/@github/img2video/videoClips/"

def convertToNanoSeconds(timeStamp):
    left = timeStamp.split(",")[0]
    nanoSeconds = int(timeStamp.split(",")[1])

    h = int(left.split(":")[0])
    m = int(left.split(":")[1])
    s = int(left.split(":")[2])

    return 1000 * (h * 60 * 60 + m * 60 + s) + nanoSeconds


def create_single_video(startTS, endTS, imgName, fps=50):
    timeSpan = convertToNanoSeconds(endTS.split(" --> ")[1]) - convertToNanoSeconds(startTS.split(" --> ")[0])
    perFrameTime = 1 / fps
    framesCount = math.ceil(timeSpan / 1000 / perFrameTime)

    createdVideoPath = pathOut + imgName.split(".")[0] + ".avi"

    # Read img
    img = cv2.imread(pathIn + imgName, cv2.IMREAD_UNCHANGED)

    # Discard alpha channel
    img = img[:,:,:3]

    # Normalize image to 720P, empty space filled with black color
    img = resize_image_720P(img)

    out = cv2.VideoWriter(createdVideoPath, cv2.VideoWriter_fourcc(*'DIVX'), 50, RES_720P)
    for i in range(framesCount):
        out.write(img)

    out.release()
