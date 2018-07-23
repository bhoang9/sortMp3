#CURRENT:
#       -Able to naively check for correct file name format and create a new
#           folder with the artist based on that simple formatting
#       -Now able to correct file names with oddly placed "-" characters

#GOALS: 
#       -Make the name correction process more robust
#       -Use given metadata to determine if the name is correct or not
#       -Have a main file and modularize these functions
import musicbrainzngs
import mutagen, os
import pathlib, shutil
import re
from tagSearch import songDataTest
from mutagen.mp3 import EasyMP3
from mutagen.easyid3 import EasyID3
from mutagen import MutagenError

musicbrainzngs.set_useragent("sortMp3", "0.1")

#get the current directory's files
os.chdir(os.getcwd() + "/music_samples_testing")
files = os.listdir(os.getcwd())
artists = []

def correctFileNames():
    for mp3File in files:
        fileIndex = files.index(mp3File)
        correctMp3File = mp3File.replace("_", " ")

        if(replaceDash(mp3File)):
            #print("match: " + match.group())
            correctMp3File = correctMp3File.replace("-", " - ")
            spaceMatch = re.search(r'\s+-\s+', correctMp3File)
            if(spaceMatch):
                correctMp3File = correctMp3File.replace(spaceMatch.group(), " - ")
                    
                #print("corrected: " + mp3File + " -> " + correctMp3File)

        os.rename(mp3File, correctMp3File)
        files[fileIndex] = correctMp3File




#runs through each file, checks for the correct format, and
#creates a new folder for that artist

def createFolders():
    for mp3_file in files:
        #if file's name contains " - ", we assume(for now), it is the artist name
        if((mp3_file.endswith('.mp3')) and (" - " in mp3_file)):
            artist = mp3_file.split(" - ", 1)[0]
            print(mp3_file)
            print("artist: " + artist + "\n")

            #if correct file format, create new folder
            #library creates new folder, handles if folder already exists
            createFolder(mp3_file, artist)

#creates a new folder with the name of "artist" variable
#moves the mp3 file into this new folder
def createFolder(mp3_file, artist):
    pathlib.Path(artist).mkdir(parents=True,exist_ok=True)
    shutil.move(mp3_file, artist+"/"+mp3_file)

#Use regex to find names w/ "w-w" format w/ "w - w" where
# w is any letter or number
def replaceDash(mp3Name):
        match0 = re.search(r'\w-\w',mp3Name)
        match1 = re.search(r'\w-\W',mp3Name)
        match2 = re.search(r'\W-\w',mp3Name)
        match3 = re.search(r'\W-\W',mp3Name)

        if(match0 or match1 or match2 or match3):
            return True
        else:
            return False
 

correctFileNames()
createFolders()
