import os
import string

def rename_files():
    file_list= os.listdir(r"C:\Users\Dragonslayer\Desktop\udacity\Programming Foundations with Python\prank\prank")
    print(file_list)
    saved_path = os.getcwd()
    print(saved_path)
    print(os.getcwd())
    os.chdir(r"C:\Users\Dragonslayer\Desktop\udacity\Programming Foundations with Python\prank\prank")
    print(os.getcwd())
    for file_name in file_list:
        os.rename(file_name, file_name.lstrip("0123456789"))
    os.chdir(saved_path)
    print(os.getcwd())
    
rename_files()