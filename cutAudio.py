from pydub import AudioSegment

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
  newAudio = newAudio[convertToNanoSeconds(t1) + 300 : convertToNanoSeconds(t2) + 300]
  newAudio.export(imgName + ".mp3", format="mp3") #Exports to a wav file in the current path.
