import os, pathlib
import tagSearch

os.chdir(os.getcwd() + "/music_tags_test")
files = os.listdir(os.getcwd())

for mp3File in files:
    print(tagSearch.getMetadata(mp3File))
