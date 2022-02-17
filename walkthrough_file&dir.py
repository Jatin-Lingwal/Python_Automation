"""Walking through the directories and sub-directories
for fetching basic information of associated files inside each directory."""
# os module helps in various operation like os.path
import os
# time module will help in format of time
import time
Main_path = input("Enter path to walk through: ")


def walking_with_you(Main_path):
    print(f"Staring walking through the directory {Main_path}: ")
    sub_dir = os.listdir(Main_path)

    for files in sub_dir:
        files_path = os.path.join(Main_path, files) # Connecting Dir with the inside file & dir (to make absolute path)
        if os.path.isfile(files_path):
            last_access = os.path.getatime(files_path) # It returns time of last access of file
            local_time = time.ctime(last_access) # it checks system time format
            size = os.path.getsize(files_path) # size of file in bytes
            print(f'File: {files_path}')
            print(f'\t:Last accessed: {local_time}')
            print(f'\tSize: {size} Bytes')
        elif os.path.isdir(files_path):# This condition will take the same above steps if there are more dirs inside the desired path
            walking_with_you(files_path)# Calling function again to print same infos

walking_with_you(Main_path)
