""""""
#
import os
# time module will us to know when was the file created
import time
Main_path = input("Enter path to walk through: ")


def walking_with_you(Main_path):
    print(f"Staring walking through the directory {Main_path}: ")
    sub_dir = os.listdir(Main_Path)

    for files in sub_dir:
        files_path = os.path.join(Main_path, files)
        if os.path.isfile(files_path):
            last_access = os.path.getatime(files_path)
            local_time = time.ctime(last_access)
            print(local_time)
            print(files_path)


