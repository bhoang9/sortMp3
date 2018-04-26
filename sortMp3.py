#currently: able to run through files and acquire song name and artist
#GOAL: in cases where mp3 file may not have metadata, somehow
#      get that metadata from the internet and assign it to that file

import musicbrainzngs
import mutagen, os #, magic
from mutagen.mp3 import EasyMP3
from mutagen import MutagenError

musicbrainzngs.set_useragent("sortMp3", "0.1")

#get the current directory's files
os.chdir(os.getcwd() + "/music_samples")
files = os.listdir(os.getcwd())

print(files)

#get audio file metadata
for mp3_file in files:
    if(mp3_file.endswith('.mp3')):
        print(mp3_file)
        try:
            audio = mutagen.File(mp3_file, None, True)
        except MutagenError:
            print("Failed to load file")
            audio.tags = []         #if file could not be loaded, wipe previous
                                    #audio tags

        if not audio.tags:          #if audio tags are empty
            print("empty tags \n")
        else:
            #print(audio.tags)
            if 'title' not in audio.tags:
                print("empty title")
            else:
                print(audio.tags['title'])
            if 'artist' not in audio.tags:
                print("empty artist")
            else:
                print(audio.tags['artist'])
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

