from zip_extract import zip_ex
from zip_creater import zip_create
import os

print("Welcome to the WinRar! ")
print("Please select your choice")
print("1. For Creating Zip")
print("2. For Extracting zip")

choice = int(input("Please enter your choice: "))
if choice == 1:
    print("You Selected Creating Zip")
    dir = input("Please enter a directory which you want to a compress: ")
    try:
        zip_create(dir)
        #Zip File will be store in folder in which you selected to compress
    except Exception as e:
        print(e)

elif choice == 2:
    print("You selected Extracting Zip")
    file_path = input('Please give directory of zip file path: ')
    file_name = input("Please choose FileName(Without Extension): ")
    fp = file_path +"/"+ file_name +'.zip'
    print("Choose a selection: ")
    print('(1) Enter 1. For current working directory: \n(2) Enter a Path where you want to Extract')
    ch = input("Enter your choice: ")
    try:
        if ch == '1':
            zip_ex(fp)
        else:
            os.chdir(ch)
            zip_ex(fp)
    except Exception as e:
        print(e)
else:
    print("Invalid choice")