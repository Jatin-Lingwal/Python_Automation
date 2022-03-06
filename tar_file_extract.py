"""Extracting a tar file to the desired location"""
import tarfile
try:
    file2_extract_path = input("Please enter the file path: ")
    where2extract_file_dest = input("Where do you want to extract the file: ")
    file_content = tarfile.open(file2_extract_path)
    file_content.extractall(where2extract_file_dest)
except FileNotFoundError:
    print("File doesn't exist")

