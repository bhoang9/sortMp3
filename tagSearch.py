#file contains function to search database for title and artist tags
#still need to test

import musicbrainzngs as musicData
import mutagen
import os
import Levenshtein
from mutagen.mp3 import EasyMP3
from mutagen.easyid3 import EasyID3
from mutagen import MutagenError

musicData.set_useragent("dataSearch_test", "0.1")

#search database for a specific artist
#result = musicData.search_artists(artist="green day")

#search database for a specific song, get first 5 results
#result2 = musicData.search_recordings("morgan page the longest road deadmau5 remix", limit=5)

#TESTING: printing from artist search
#for artists in result['artist-list']:
#        print(artists['name'])

#TESTING: if search yields no results
#if(result2['recording-list'] == []):
#    print("empty")

#TESTING: printing from song search
#for recordings in result2['recording-list']:
#        print(recordings['title'] + " | artist " + recordings['artist-credit-phrase'])


#Get song's current metadata
def getMetadata(mp3_file):
    metaData = []

    try:
        audio = EasyID3(mp3_file)
    except MutagenError:
        print("Failed to load file \n")
        return None

    if not audio:
        return None
    elif 'title' not in audio:
        return None
    elif 'artist' not in audio:
        return None

    #set the title and artist of the song as elements 0 and 1 of the list
    #respectively
    else:
        metaData.append(audio['title'][0].replace(" ", "").lower())
        metaData.append(audio['artist'][0].replace(" ","").lower())
        metaData.append(audio['title'][0])
        metaData.append(audio['artist'][0])

        return metaData

def checkMetaData(mp3_file):
    
    givenArtist = mp3_File.slit(" - ",1)[0].lower()
    givenSong = mp3File.split(" - ",1)[1].lower()
    metaData = getMetadata(mp3_file)
    metaDataReturn = []

    if(Levenshtein.ratio(givenArtist, metaData[0]) == 0):
        metaDataReturn.append(metaData[2])
        metaDataReturn.append(metaData[3])

    return metaDataReturn


#function: Get correct song tags given song and artist name
#givenArtist would ideally be provided from the parsed file string
#songName would be given in a similar fashion
def getSongData(songName, givenArtist):

    songTags = {'Name': "", 'Artist':""}
    songData = musicData.search_recordings(songName, limit=5)

    #run through the data given by the query
    for songData in songData['recording-list']:
        #if the artist matches the function parameter, then those are the tags wanted
        if(songData['artist-credit-phrase'].lower() == givenArtist.lower()):
            songTags['Name'] = songData['title']
            songTags['Artist'] = songData['artist-credit-phrase']
            break

    #if no match was found, don't return anything
    if(songTags['Name'] == ""):
        return None
    #if we found the correct match, return the songTags dictionary

    else:
        return songTags
   
def songDataTest(songName):
    songData = musicData.search_recordings(songName, limit=5)

    for songData in songData['recording-list']:
        if(songData == []):
            print("empty")
        else:
            print("title: " + songData['title'] + " | artist: " + songData['artist-credit-phrase'])

