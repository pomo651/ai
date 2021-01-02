from pydub import AudioSegment
t1 = 23296
t2 = 28928
newAudio = AudioSegment.from_mp3("output.mp3")
newAudio = newAudio[t1:t2]
newAudio.export('segment4.mp3', format="mp3") #Exports to a wav file in the current path.