#Currently: able to run through files and acquire song name and artist
#           able to acquire metadata from an internet database

#GOAL:      Need to decide on how to determine how and when to search
#           database for information

#BUG: currently EasyID3 is not airtight in determining when it has enough data for lookup 

import musicbrainzngs
import mutagen, os
from tagSearch import songDataTest
from mutagen.mp3 import EasyMP3
from mutagen.easyid3 import EasyID3
from mutagen import MutagenError

musicbrainzngs.set_useragent("sortMp3", "0.1")

#get the current directory's files
os.chdir(os.getcwd() + "/music_samples")
files = os.listdir(os.getcwd())

#print(files)

#get audio file metadata
for mp3_file in files:
    if(mp3_file.endswith('.mp3')): 
        print(mp3_file)
        try:
            #audio = mutagen.File(mp3_file, None, True)
            audio = EasyID3(mp3_file)
        except MutagenError:
            print("Failed to load file")
            continue
            #audio.tags = []         #if file could not be loaded, wipe previous
                                    #audio tags

        #if not audio.tags:
        #   print("empty tags \n")
        if not audio:
            print("empty tags \n")
        elif not audio['title']:
            print("empty tags \n")
        elif not audio['artist']:
            print("empty tags \n")
        else:
            #if 'title' not in audio.tags:
            #    print("no title tag")
            #else:
                #songDataTest(audio.tags['title'])
            songDataTest(audio['title'])

#        if not audio.tags:          #if audio tags are empty
#            print("empty tags \n")
#        else:
            #print(audio.tags)
#            if 'title' not in audio.tags:
#                print("empty title")
#            else:
#                print(audio.tags['title'])
#            if 'artist' not in audio.tags:
#                print("empty artist")
#            else:
#                print(audio.tags['artist'])
        print("\n") 


