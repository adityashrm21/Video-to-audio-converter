#!/usr/bin/env python3

import urllib.request
import urllib.error

import re
import sys
import time
import os

def video_to_audio(fileName):

	try:
		os.rename(fileName, 'audio.mp4')
		video_to_wav = 'ffmpeg -i '+'audio.mp4'+' '+'audio.wav'
		final_audio ='lame '+'audio.wav'+' '+'audio.mp3'
		os.system(video_to_wav)
		os.system(final_audio)
		os.remove('audio.wav')
		print("sucessfully converted ",fileName, " into audio!")
	except OSError as err:
		print(err.reason)
		exit(1)


def main():
    if len(sys.argv) <1 or len(sys.argv) > 2:
        print('command usage: python video_to_audio.py FilePath')
        exit(1)
    else:
        filePath = sys.argv[1]
    
        # check if the specified file exists or not
        try:
            if os.path.exists(filePath):
            	print("file found!")
        except OSError as err:
            print(err.reason)
            exit(1)


        # convert video to audio
        video_to_audio(filePath)
        time.sleep(1)

# install ffmpeg and/or lame if you get an error saying that the program is currently not installed 

if __name__ == '__main__':
    main()