import os

path = "/Users/binyugao/@github/ai/media"
directory = os.fsencode(path)
    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     print(filename)

     