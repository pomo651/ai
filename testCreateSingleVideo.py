import re
import sys
sys.path.insert(1, "/Users/binyugao/@github/img2video")

# Self
from img2video import create_single_video

def main():
    prevTimeStamp = "00:00:00,256 --> 00:00:04,096"
    curTimeStamp = "00:00:07,168 --> 00:00:08,704"
    media = "a1.jpg"

    # 将prevMedia 此时做成processedVideo 并且放好
    create_single_video(prevTimeStamp, curTimeStamp, media)

main()
