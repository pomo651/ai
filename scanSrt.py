import re
import sys
sys.path.insert(1, "/Users/binyugao/@github/img2video")

# Self
from img2video import create_single_video

def main():
    prevTimeStamp = "00:00:00,000 --> 00:00:00,000"
    curTimeStamp = "00:00:00,000 --> 00:00:00,000"
    prevMedia = ""

    # read file line by line
    file = open( "output.srt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        if "-->" in line: # Upda
            curTimeStamp = line


        if ".jpg" in line: # 碰到mediaFile后是将之前的Media做好排序

            # 将prevMedia 此时做成processedVideo 并且放好
            if len(prevMedia) > 0:
                create_single_video(prevTimeStamp, curTimeStamp, prevMedia)

            # 更新media
            prevMedia = line.strip()

            # 更新TimeStamp
            prevTimeStamp = curTimeStamp

    # 处理Last media, read to last line
    create_single_video(prevTimeStamp, curTimeStamp, prevMedia)
    

main()
