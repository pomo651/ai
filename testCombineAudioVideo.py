import math 
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def combine_audio(vidname, audname, outname, fps=25):
    import moviepy.editor as mpe
    audio_background = mpe.AudioFileClip(audname)
    my_clip = mpe.VideoFileClip(vidname)
    duration = audio_background.duration

    print(duration)
    final_clip = my_clip.set_audio(audio_background).set_duration(duration)

    # final_clip = final_clip.set_duration(duration + 0.1)

    # ffmpeg_extract_subclip( final_clip, 0, duration, targetname=outname)

    final_clip.write_videofile(outname,fps=fps)


def main():
  video = "/Users/binyugao/@github/ai/aa.mp4"
  audio = "/Users/binyugao/@github/ai/segment1.mp3"
  combine_audio(video, audio, "work1.mp4")


main()

