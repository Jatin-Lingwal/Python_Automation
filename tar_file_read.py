"""This help us to read tar file"""
import tarfile
try:

    file_path = input("Enter path to read the desired archived file: ")
    File_content = tarfile.open(file_path, 'r') # Opening the file.

    for files in File_content.getnames(): # Getnames() helps to show all the content in tar file in list format.
        print(files)

except FileNotFoundError:
    print("File Path doesn't exist")
else:
    print("Read the tar file successfully")
