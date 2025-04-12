#!/usr/bin/env python3

'''Remove duplicate .eml files from a given directory'''

from datetime import datetime
from os import listdir, path, remove

from tqdm import tqdm


def remove_duplicates(directory):
    '''Remove duplicate .eml files from directory'''
    file_names = set()
    files = duplicates = 0
    directory_path = path.realpath(directory)
    for file_name in tqdm(listdir(directory_path)):
        if file_name[-4:] != ".eml":
            continue
        files += 1
        potential_duplicate_part = file_name.split(".", maxsplit=1)[0]
        if potential_duplicate_part in file_names:
            remove(path.join(directory_path, file_name))
            duplicates += 1
        else:
            file_names.add(potential_duplicate_part)
    return files, duplicates

def log_usage(start_time, files, duplicates):
    '''Log start time, run time, files reviewed, and duplicates removed'''
    file_name = "usage_log.csv"
    run_time = datetime.now() - start_time
    if path.isfile(file_name):
        with open(file_name, "a", encoding='UTF-8') as file:
            file.write(f"{start_time},{run_time},{files},{duplicates}\n")
    else:
        with open(file_name, "x", encoding='UTF-8') as file:
            file.write("start time,run time,files scanned,duplicates\n")
            file.write(f"{start_time},{run_time},{files},{duplicates}\n")

def main():
    '''Remove duplicates, log usage info'''
    directory = input("Enter the full path to the folder which contains the EMLs: ").strip('"')
    start_time = datetime.now()
    files, duplicates = remove_duplicates(directory)
    print(f"Removed {duplicates} duplicate .eml file{"s" if duplicates != 1 else ""}")
    log_usage(start_time, files, duplicates)

if __name__ == "__main__":
    main()
