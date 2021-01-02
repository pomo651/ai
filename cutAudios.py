import re
import sys
from pydub import AudioSegment
import ffmpeg
from moviepy.editor import VideoFileClip, concatenate_videoclips
sys.path.insert(1, "/Users/binyugao/@github/img2video")

from resizeImg import resize_image_720P

media = []

def convertToNanoSeconds(timeStamp):
    left = timeStamp.split(",")[0]
    nanoSeconds = int(timeStamp.split(",")[1])

    h = int(left.split(":")[0])
    m = int(left.split(":")[1])
    s = int(left.split(":")[2])

    return 1000 * (h * 60 * 60 + m * 60 + s) + nanoSeconds


def cut_audio_clip(startTS, endTS, imgName):
  t1 = startTS.split(" --> ")[1]
  t2 = endTS.split(" --> ")[1] 
  print("clip %s if from %s to %s" %(imgName, t1, t2))

  newAudio = AudioSegment.from_mp3("output.mp3")
  newAudio = newAudio[convertToNanoSeconds(t1) + 50 : convertToNanoSeconds(t2) - 50]
  newAudio.export("/Users/binyugao/@github/ai/media/" + imgName + ".mp3", format="mp3") #Exports to a wav file in the current path.


def combine_image_audio(f):
  input_still = ffmpeg.input("/Users/binyugao/@github/ai/media/" + f)
  input_audio = ffmpeg.input("/Users/binyugao/@github/ai/media/" + f + ".mp3")

  (
    ffmpeg
    .concat(input_still, input_audio, v=1, a=1)
    .output("/Users/binyugao/@github/ai/media/" + f + ".mp4")
    .run(overwrite_output=True)
  )


def combine_audio_video(f, fps=25):
  import moviepy.editor as mpe
  video_path = "/Users/binyugao/@github/ai/media/" + f
  audio_path = "/Users/binyugao/@github/ai/media/" + f + ".mp3"
  output_path = "/Users/binyugao/@github/ai/media/" + f + ".mp4"

  audio_background = mpe.AudioFileClip(audio_path)
  my_clip = mpe.VideoFileClip(video_path)
  duration = audio_background.duration

  final_clip = my_clip.set_audio(audio_background).set_duration(duration)
  final_clip.write_videofile(output_path, fps=fps)


def main():
  prevTimeStamp = "00:00:00,000 --> 00:00:00,000"
  curTimeStamp = "00:00:00,000 --> 00:00:00,000"
  prevMedia = ""

  # read file line by line
  file = open( "output.srt", "r")
  lines = file.readlines()
  file.close()

  for line in lines:
      if "-->" in line: 
          curTimeStamp = line

      file_types = [".jpg", ".mp4"]
      # if ".jpg" in line: # 碰到mediaFile后是将之前的Media做好排序

      if any(f in line for f in file_types):

          # 将prevMedia 此时做成processedVideo 并且放好
          if len(prevMedia) > 0:
              media.append(prevMedia)
              cut_audio_clip(prevTimeStamp, curTimeStamp, prevMedia)

          # 更新media
          prevMedia = line.strip()

          # 更新TimeStamp
          prevTimeStamp = curTimeStamp

  # 处理Last media, read to last line
  cut_audio_clip(prevTimeStamp, curTimeStamp, prevMedia)
  media.append(prevMedia)
  
  print(media)

  # combine each image with audio into one video clip
  for f in media:
    if ".jpg" in f:
      combine_image_audio(f)
    if ".mp4" in f:
      combine_audio_video(f)

  # merge video clips into one 
  clips = []
  for f in media:
    clipPath = "/Users/binyugao/@github/ai/media/" + f + ".mp4"
    # if not ".mp4" in f:
    #   clipPath = clipPath + ".mp4"
    clips.append(VideoFileClip(clipPath))    

  final_video = concatenate_videoclips(clips)
  final_video.write_videofile("/Users/binyugao/@github/ai/media/final.mp4")
  
      
main()
