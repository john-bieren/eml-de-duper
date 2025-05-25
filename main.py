#!/usr/bin/env python3

'''Remove duplicate .eml files from a given directory'''

from datetime import datetime
from os import listdir, mkdir, path, remove
from shutil import move

from tqdm import tqdm

from exception_logger import configure_logger

configure_logger()

def main():
    '''Remove duplicates, log usage info'''
    directory = input("Enter the full path to the folder which contains the EMLs: ").strip('"')
    directory_path = path.realpath(directory)

    while True:
        y_n = input('Move duplicates to a "duplicates" subfolder instead of deleting them? (y/n) ')
        if y_n.strip().lower() in ('y', 'n'):
            break
        print(f'"{y_n}" is an invalid input, please respond with either "y" or "n"')
    keep_files = y_n.strip().lower() == 'y'

    start_time = datetime.now()
    emls_scanned, duplicates = remove_duplicates(directory_path, keep_files)
    run_time = datetime.now() - start_time

    word = "Moved" if keep_files else "Removed"
    print(f"{word} {duplicates} duplicate .eml file{"s" if duplicates != 1 else ""}")
    log_usage(start_time, run_time, emls_scanned, duplicates, y_n, directory_path)

def remove_duplicates(directory_path, keep_files):
    '''Remove duplicate .eml files from directory'''
    if keep_files:
        dup_dir_path = path.join(directory_path, "duplicates")
        if not path.exists(dup_dir_path):
            mkdir(dup_dir_path)

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

        if potential_duplicate_part in file_names:
            if keep_files:
                move(path.join(directory_path, file_name), path.join(dup_dir_path, file_name))
            else:
                remove(path.join(directory_path, file_name))
            duplicates += 1
        else:
            file_names.add(potential_duplicate_part)
    return emls_scanned, duplicates

def log_usage(start_time, run_time, emls, duplicates, dups_moved, dir_path):
    '''Log info about the usage of the program'''
    file_name = "usage_log.csv"
    if path.isfile(file_name):
        with open(file_name, "a", encoding='UTF-8') as file:
            file.write(f'{start_time},{run_time},{emls},{duplicates},{dups_moved},"{dir_path}"\n')
    else:
        with open(file_name, "x", encoding='UTF-8') as file:
            file.write("start time,run time,emls scanned,duplicates,duplicates moved,directory\n")
            file.write(f'{start_time},{run_time},{emls},{duplicates},{dups_moved},"{dir_path}"\n')

if __name__ == "__main__":
    main()
