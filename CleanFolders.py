
                 
import json
import os
from os import listdir
from os.path import isfile, join
folder_path= r"C:\Users\YourFolder" + "\\"
json_file=r"C:\Users\dictionary.json"
onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
if onlyfiles:
    for file in onlyfiles:
        extension = os.path.splitext(file)[1]
        with open (json_file, "r") as dict:
            my_dict=json.load(dict)
        if extension in my_dict.keys():
            foldername=my_dict[extension]
            if os.path.exists(folder_path + foldername):
                os.rename(folder_path + file, os.path.join(folder_path + foldername, os.path.basename(file)))
            else:
                os.makedirs(folder_path + foldername)
                os.rename(folder_path + file, os.path.join(folder_path + foldername, os.path.basename(file))) 

        else:
            new_extension=input(f"Extension {extension} doesn't have a valid folder. Under what folder name you want to move the file? ")
            my_dict[extension] = new_extension
            with open (json_file, "w") as dict:
                json.dump(my_dict,dict)
            os.makedirs(folder_path + new_extension)
            os.rename(folder_path + file, os.path.join(folder_path + new_extension, os.path.basename(file)))
else:
    print("There are no files. The program will exit")



        















    

