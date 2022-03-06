"""Reading and extracting tar file to the desired location"""

from tarfile import TarFile
try:
    file_path = input("Enter the required path: ")
    destination_path = input("Enter the required path:")

    with TarFile(file_path, 'r') as myfile:
        for lines in myfile.getnames(): # Getnames() helps to show all the content in tar file in list format.
            print(lines)
        file_cont_ext = myfile.extractall(destination_path)
        print("File got extracted successfully!")
except FileNotFoundError:
    print("Wrong file or path entered!")

