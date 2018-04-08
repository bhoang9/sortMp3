#currently: parsing mp3 files and getting their metadata
#TODO: in cases where mp3 file may not have metadata, somehow
#      get that metadata from the internet and assign it to that file

import mutagen, os, magic
from mutagen.mp3 import EasyMP3
from mutagen import MutagenError


#get the current directory's files
os.chdir(os.getcwd() + "/music_samples")
files = os.listdir(os.getcwd())

print(files)

#get audio file metadata
for mp3_file in files:
    if(mp3_file.endswith('.mp3')):
        print(mp3_file)
        audio = mutagen.File(mp3_file, None, True)
        print(audio.tags)
        print("\n") 
        #print(audio.tags['title'])
        #print(audio.tags['artist'])

#try:
#    audio = mutagen.File("test_folder", None, True)
#except MutagenError:
#    print("That's not an mp3 file!")

#print(audio.tags['title'])

#print(audio1.tags['title'])
#print(audio2.tags['title'])

