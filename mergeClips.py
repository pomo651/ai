from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
from os.path import isfile, join

import sys
sys.path.insert(1, "/Users/binyugao/@github/img2video")

clipsFolder = "./videoClips"

def excludeFile(f):
    return f[0] != '.'

files = [f for f in os.listdir(clipsFolder) if excludeFile(f)]
files.sort()

clips = []

for i in range(len(files)):
    file = files[i]
    print(file)
    clipPath = clipsFolder + "/" + file
    clips.append(VideoFileClip(clipPath))

final_video = concatenate_videoclips(clips)
final_video.write_videofile("/Users/binyugao/@github/img2video/videoClips/final_video.mp4")
