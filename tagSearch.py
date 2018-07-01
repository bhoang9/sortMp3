#file contains function to search database for title and artist tags
#still need to test

import musicbrainzngs as musicData
import os

musicData.set_useragent("dataSearch_test", "0.1")

#search database for a specific artist
result = musicData.search_artists(artist="green day")

#search database for a specific song, get first 5 results
result2 = musicData.search_recordings("welcome to paradise", limit=5)

#for songName in zip(range(5),result2['recording-list']):
#    print(songName["title"])

for artists in result['artist-list']:
        print(artists['name'])

for recordings in result2['recording-list']:
        print(recordings['title'] + "| artist " + recordings['artist-credit-phrase'])

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
    
