#!/usr/bin/env python3

"""Move potential duplicate .eml files from a given directory into a subdirectory"""

from datetime import datetime
from os import listdir, mkdir, path
from shutil import move

from tqdm import tqdm

from exception_logger import configure_logger

configure_logger()

def main():
    """Move potential duplicates, log usage info"""
    directory = input("Enter the full path to the folder which contains the EMLs: ").strip('"')
    directory_path = path.realpath(directory)

    start_time = datetime.now()
    emls_scanned, duplicates = move_duplicates(directory_path)
    run_time = datetime.now() - start_time

    print(f"Moved {duplicates} potential duplicate .eml file{"s" if duplicates != 1 else ""}")
    log_usage(start_time, run_time, emls_scanned, duplicates, directory_path)

def move_duplicates(directory_path):
    """Move potential duplicate .eml files to a subdirectory"""
    # find/make path for potential duplicates directory
    dup_dir_path = path.join(directory_path, "Potential Duplicates")
    if not path.exists(dup_dir_path):
        mkdir(dup_dir_path)

    # process file names, handle potential duplicates
    file_names = set()
    emls_scanned = duplicates = 0
    for file_name in tqdm(listdir(directory_path)):
        if file_name[-4:] != ".eml":
            continue
        emls_scanned += 1

        # there are two possible file name formats
        if "." in file_name.replace(".eml", ""):
            # 1999-12-31T23_59_59.000Z_123
            split_char = "."
        else:
            # 19991231235959_123
            split_char = "_"
        potential_duplicate_part = file_name.split(split_char, maxsplit=1)[0]

        # check whether the file may be a duplicate, handle it accordingly
        if potential_duplicate_part in file_names:
            move(path.join(directory_path, file_name), path.join(dup_dir_path, file_name))
            duplicates += 1
        else:
            file_names.add(potential_duplicate_part)
    return emls_scanned, duplicates

def log_usage(start_time, run_time, emls, duplicates, dir_path):
    """Log info about the usage of the program"""
    file_name = "v2_usage_log.csv"
    if path.isfile(file_name):
        with open(file_name, "a", encoding="UTF-8") as file:
            file.write(f'{start_time},{run_time},{emls},{duplicates},"{dir_path}"\n')
    else:
        with open(file_name, "x", encoding="UTF-8") as file:
            file.write("Start Time,Run Time,EMLs Scanned,Potential Duplicates,Directory\n")
            file.write(f'{start_time},{run_time},{emls},{duplicates},"{dir_path}"\n')

if __name__ == "__main__":
    main()
