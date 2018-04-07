import mutagen,os
from mutagen.mp3 import EasyMP3

files = os.listdir(os.getcwd())

print(files)

#get audio file metadata
audio = mutagen.File("nujabes.mp3", None, True)
audio1 = mutagen.File("InTheEnd.mp3", None, True)
#audio2 = mutagen.File("pianoMan.mp3")

print(audio.tags)
#print(audio['TPE1'])
#print(audio['TIT2'])

print(audio1.tags)


#print(audio1['TIT2'])
#print(audio2['TPE1'])
#print(audio2['TIT2'])
