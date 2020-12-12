"""
Convert all sentences found in txt files from a directory in .mp3 files
"""

import os 
from sys import argv
import mimetypes
import pyttsx3

MAX_NR_SENTENCES = 100
MAX_LENGTH_SENTENCE = 100

USAGE_MSG = f"""Usage: python {argv[0]} <dir_text_files> <dir_save_mp3>
    <dir_text_files> - dir with multiple text files that has sentence/line
    <dir_save_mp3>   - dir to save conversion of sentences in mp3 files
WARNINGS: 
    MAX LENGTH SENTENCE: {MAX_LENGTH_SENTENCE} (sentence with more than that will be ignore)
    MAX NR SENTENCES: {MAX_NR_SENTENCES} (the program will stop when convert the maximum number of sentences)""" 


def check_dir(dir_path):
    if not os.path.exists(dir_path):
        print(f"[ERROR] Doesn't exist this path: {dir_path} \n")
        raise SystemExit

    if not os.path.isdir(dir_path):
        print(f"[ERROR] {dir_path} is not a directory\n")
        raise SystemExit

def check_max_length_sentence(sentence):
    return len(sentence) <= MAX_LENGTH_SENTENCE

def get_engine_voice():

    engine = pyttsx3.init()
    # RATE
    engine.setProperty('rate', 150)
    # VOICE
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)

    return engine

def write_mp3_file(sentence, dir_path, index_sentence):
    print(os.path.join(dir_path, f"sound{index_sentence}.mp3"))
    engine = get_engine_voice()
    engine.save_to_file(sentence, os.path.join(dir_path, f"sound{index_sentence}.mp3"))
    engine.runAndWait()

def convert_sentences(dir_text_files, dir_save_mp3):
    count_sentences = 0

    for root, subdirs, files in os.walk(dir_text_files):
        for _file in files:
            path_to_file = os.path.join(root, _file)
            if mimetypes.guess_type(path_to_file)[0] == "text/plain":
                with open(path_to_file, "r") as read_file:
                    while True:
                        line = read_file.readline().strip()
                        if not line:
                            break
                        if check_max_length_sentence(line) == True:
                            count_sentences += 1
                            if count_sentences > MAX_NR_SENTENCES:
                                print(f"\n[WARNING] The program stop execution at file: {path_to_file} because the maximum number of sentences was exceeded.\n")
                                raise SystemExit
                            write_mp3_file(line, dir_save_mp3, count_sentences)

    if count_sentences == 0:
        print(f"\n[WARNING] No mp3 file was created, because no sentence was found with max length: {MAX_LENGTH_SENTENCE}.\n")
                            
if __name__ == "__main__":
    
    if len(argv) != 3:
        print("[ERROR] Invalid number of arguments...")
        print(USAGE_MSG)
        raise SystemExit
    
    dir_text_files = argv[1]
    dir_save_mp3 = argv[2]

    check_dir(dir_text_files)
    check_dir(dir_save_mp3)

    convert_sentences(dir_text_files, dir_save_mp3)