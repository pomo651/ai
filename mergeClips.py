from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
from os.path import isfile, join

import sys
sys.path.insert(1, "/Users/binyugao/@github/ai")

mediaFolder = "./media"

def excludeFile(f):
    return f[0] != '.' 

files = [f for f in os.listdir(mediaFolder) if excludeFile(f)]
files.sort()


clips = []
for f in files:
    if ".mp4" in f:
        clips.append(VideoFileClip("/Users/binyugao/@github/ai/media/" + f))      

print(clips)


# for i in range(len(files)):
#     file = files[i]
#     print(file)
#     clipPath = clipsFolder + "/" + file
#     clips.append(VideoFileClip(clipPath))

final_video = concatenate_videoclips(clips)
final_video.write_videofile("/Users/binyugao/@github/ai/media/final_video.mp4")
