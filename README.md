# Video-to-audio-converter
A python script to convert video files into mp3 audio files. As a heavy listener of music, I prefer keeping audio files on my phone than video files to consume less disk space. This tool helps in converting the video files present in my computer to mp3 audio files.


### Requirements:


##### This script needs Python 3+

If you don't have Python 3 installed, you just need to install python3 package :

```bash
$ sudo apt-get install python3
```

### Clone:
```bash
$ git clone https://github.com/adityashrm21/Video-to-audio-converter
$ cd ../Video-to-audio-converter
```

### Usage:

```bash
$ python3 video_to_audio.py <filename>
```

### Other Prerequisites
Make sure you install ffmpeg (specially on Windows). You may encounter an error referred to ffmpeg not being installed 

#### macOS:
Install FFmpeg using Homebrew:
```
brew install ffmpeg
```
#### Linux:
Install FFmpeg using the package manager for your distribution. For example, on Ubuntu, you would run:

```
sudo apt-get update
sudo apt-get install ffmpeg
```
 #### Verify FFmpeg Installation
```
ffmpeg -version

```