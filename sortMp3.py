#CURRENT: able to naively check for correct file name format and create a new
#         folder with the artist based on that simple formatting

#GOAL: rename files if they are in the wrong format 

import musicbrainzngs
import mutagen, os
import pathlib, shutil
from tagSearch import songDataTest
from mutagen.mp3 import EasyMP3
from mutagen.easyid3 import EasyID3
from mutagen import MutagenError

musicbrainzngs.set_useragent("sortMp3", "0.1")

#get the current directory's files
os.chdir(os.getcwd() + "/music_samples_testing")
files = os.listdir(os.getcwd())
artists = []

#print(files)

#get audio file metadata
for mp3_file in files:
    if((mp3_file.endswith('.mp3')) and (" - " in mp3_file)):
        artist = mp3_file.split(" - ", 1)[0]
        print(mp3_file)
        print("artist: " + artist + "\n")

        #if correct file format, create new folder
        #library creates new folder, handles if folder already exists
        pathlib.Path(artist).mkdir(parents=True,exist_ok=True)
        shutil.move(mp3_file, artist+"/"+mp3_file) #move file to new folder

