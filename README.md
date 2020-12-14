# py_project_phrase_to_sound
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is for Python Course 2020-2021.
	
## Technologies
Project is created with:
* Python 3.60
* pyttsx3 library version: 2.90
	
## Setup
You can play with 2 different scripts:
* I. convert_to_sound.py
        1. run this script with 2 parameters: convert_to_sound.py <dir1> <dir2>
            <dir1> - input directory with text files or others subdirectories that have text_files/subdirectories and so on;
                - each text file has multiple sentences (0 or more); one sentence/line
                - each sentence from all txt files found in this directory and subdirectories will be converted in audio speech and save in a mp3 files;
            <dir2> - all mp3 files will be saved in this output directory

* II. play_phrase.py
        - run this script and you see a GUI window with a textbox input for writing all you want. After you write some input text(only in english) click on the button Play and you'll hear the spoken text.
