import ffmpeg

input_still = ffmpeg.input("a1.jpg")
input_audio = ffmpeg.input("a1.jpg.mp3")

(
    ffmpeg
    .concat(input_still, input_audio, v=1, a=1)
    .output("a1.mp4")
    .run(overwrite_output=True)
)