import os
folders = input("Please provide list of folder name with space in between:").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError: 
        print("please provide a valid foldername.")
        break
    
        print("listing files for the folder :" + folder)

    for file in files:
        print(file)

