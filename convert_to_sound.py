"""
Convert all sentences found in txt files from a directory in .mp3 files
"""

from os import walk as os_walk
from os import  path as os_path
from sys import argv

USAGE_MSG = f"Usage: python {argv[0]} <dir_text_files> <dir_save_mp3>\n"

def check_dir(dir_path):
    if not os_path.exists(dir_path):
        print(f"[ERROR] Doesn't exist this path: {dir_path} \n")
        raise SystemExit

    if not os_path.isdir(dir_path):
        print(f"[ERROR] {dir_path} is not a directory\n")
        raise SystemExit

def convert_sentences(dir_text_files, dir_path):
    for root, subdirs, files in os_walk(dir_text_files):
        pass
        

if __name__ == "__main__":
    
    if len(argv) != 3:
        print("[ERROR] Invalid number of arguments...\n")
        print(USAGE_MSG)
        raise SystemExit
    
    dir_text_files = argv[1]
    dir_save_mp3 = argv[2]

    check_dir(dir_text_files)
    check_dir(dir_save_mp3)

    convert_sentences(dir_text_files, dir_save_mp3)

    # for root, subdir, files in os_walk(".", topdown=False):
    #     pass