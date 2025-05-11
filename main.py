#!/usr/bin/env python3

'''Remove duplicate .eml files from a given directory'''

from datetime import datetime
from os import listdir, path, remove

from tqdm import tqdm

from exception_logger import configure_logger

configure_logger()

def remove_duplicates(directory_path):
    '''Remove duplicate .eml files from directory'''
    file_names = set()
    emls_scanned = duplicates = 0
    for file_name in tqdm(listdir(directory_path)):
        if file_name[-4:] != ".eml":
            continue
        emls_scanned += 1

        # there are two possible formats
        if "." in file_name.replace(".eml", ""):
            # 1900-01-01T23_59_59.000Z_123
            split_char = "."
        else:
            # 19000101235959_123
            split_char = "_"
        potential_duplicate_part = file_name.split(split_char, maxsplit=1)[0]

        if potential_duplicate_part in file_names:
            remove(path.join(directory_path, file_name))
            duplicates += 1
        else:
            file_names.add(potential_duplicate_part)
    return emls_scanned, duplicates

def log_usage(start_time, run_time, emls_scanned, duplicates, directory_path):
    '''Log start time, run time, emls scanned, and duplicates removed'''
    file_name = "usage_log.csv"
    if path.isfile(file_name):
        with open(file_name, "a", encoding='UTF-8') as file:
            file.write(f'{start_time},{run_time},{emls_scanned},{duplicates},"{directory_path}"\n')
    else:
        with open(file_name, "x", encoding='UTF-8') as file:
            file.write("start time,run time,emls scanned,duplicates,directory\n")
            file.write(f'{start_time},{run_time},{emls_scanned},{duplicates},"{directory_path}"\n')

def main():
    '''Remove duplicates, log usage info'''
    directory = input("Enter the full path to the folder which contains the EMLs: ").strip('"')
    directory_path = path.realpath(directory)
    start_time = datetime.now()
    emls_scanned, duplicates = remove_duplicates(directory_path)
    run_time = datetime.now() - start_time
    print(f"Removed {duplicates} duplicate .eml file{"s" if duplicates != 1 else ""}")
    log_usage(start_time, run_time, emls_scanned, duplicates, directory_path)

if __name__ == "__main__":
    main()
