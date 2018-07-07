#Currently: able to run through files and acquire song name and artist
#           able to acquire metadata from an internet database

#GOAL:      Need to decide on how to determine how and when to search
#           database for information

#CURRENT: able to look at tags and determine if artist or title tag is found in the filename

import musicbrainzngs
import mutagen, os
from tagSearch import songDataTest
from mutagen.mp3 import EasyMP3
from mutagen.easyid3 import EasyID3
from mutagen import MutagenError

musicbrainzngs.set_useragent("sortMp3", "0.1")

#get the current directory's files
os.chdir(os.getcwd() + "/music_samples_small")
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

        #check if metadata was acquired
        if not audio:               #sometimes mutagen generates an empty dictionary
            print("empty tags \n")
        elif 'title' not in audio: 
            print("empty tags \n")  #covers case where tags are not empty, but 'title' is
        elif 'artist' not in audio: #case where tags not empty, but 'artist' is
            print("empty tags \n")

        #case that valid metadata was found
        else:
            #print(audio)
            
            #modifying file name and metadata strings to better look for substring
            fileName = mp3_file.replace(".mp3", "").replace(" ", "").lower() #can be done w/ regex, maybe later
            metadataTitle = audio['title'][0].replace(" ","").lower()
            metadataArtist = audio['artist'][0].replace(" ","").lower()
            #if metadata string is found in the file name, we know that the metadata is correct
            if (metadataTitle in fileName or metadataArtist in fileName):
                print("Song: " + audio['title'][0] + " | Artist: " + audio['artist'][0])
                
            #songDataTest(audio['title'])

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


