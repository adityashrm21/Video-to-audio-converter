#!/usr/bin/env python3

import os
import sys
import shlex
import subprocess


def video_to_audio(file_path, output_format='mp3'):
    try:
        # Check the file extension
        file_name, file_extension = os.path.splitext(file_path)

        # Properly escape the file names
        file_name_escaped = shlex.quote(file_name)
        file_path_escaped = shlex.quote(file_path)

        # Set up output file name and command
        if output_format == 'wav':
            output_file = f"{file_name_escaped}.wav"
            command = f"ffmpeg -i {file_path_escaped} {output_file}"
        elif output_format == 'mp3':
            output_file = f"{file_name_escaped}.mp3"
            command = f"ffmpeg -i {file_path_escaped} -q:a 0 {output_file}"
        else:
            print(f"Unsupported output format: {output_format}")
            return

        # Execute the command
        print(f"Converting {file_path} to {output_format} format...")
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully converted {file_path} to {output_file}!")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during conversion: {e}")
        sys.exit(1)
    except OSError as err:
        print(f"OS error: {err}")
        sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print('Usage: python3 video_to_audio.py <FilePath> <OutputFormat>')
        print('OutputFormat should be either "mp3" or "wav"')
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        output_format = sys.argv[2]

        # Check if the specified file exists or not
        if not os.path.exists(file_path):
            print(f"File {file_path} not found!")
            sys.exit(1)

        # Convert video to audio
        video_to_audio(file_path, output_format)


if __name__ == '__main__':
    main()
