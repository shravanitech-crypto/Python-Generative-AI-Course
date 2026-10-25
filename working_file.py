## Creating new directory using os module
import os
'''
new_directory = "packages"
os.mkdir(new_directory)
print(f"Directory '{new_directory}' created successfully.")

## Listing all directories and files

items= os.listdir('.')
print(items)



## joinng path

directory = "packages"
file_name = "sample.txt"
path= os.path.join(directory, file_name)
print("path:",path)

##get with folder location
directory = "packages"
file_name = "sample.txt"
path = os.path.join(os.getcwd(),directory, file_name)

### Check if the file exists
path = "destination.txt"
if os.path.exists(path):
    print(f"The '{path}' file exists")
else:
    print(f"The '{path}' file does not exist")
    '''
## Check whether the given path is a file or directory
path = "sample.txt/packages"
if os.path.isfile(path):
    print(f"The '{path}' is a file")
elif os.path.isdir(path):
    print(f"The '{path}' is a directory")
else:
    print(f"The '{path}' is neither a file nor a directory")