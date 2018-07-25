import mp3Names
import tagSearch
import os, pathlib, shutil

os.chdir(os.getcwd() + "/music_samples_testing")
files = os.listdir(os.getcwd())
artists = []

def main():
    mp3Names.correctFileNames(files)
    mp3Names.createFolders(files)


#main()

