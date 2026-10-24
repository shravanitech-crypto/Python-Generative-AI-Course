## Read whole file
'''
with open ('sample.txt', 'r') as file:
    x = file.read()
    print(x)
    '''
'''
## Read file line by line
with open ('sample.txt','r') as file:
    for line in file:
        print(line.strip())

## Writing a file (overwrtting)
with open ('sample.txt', 'w') as file:
    file.write("Welcome You All")

## Write a file (without overwriting)
with open ('sample.txt','a') as file:
    file.write("\nWelcome to Python Programming")

## write multiple lines to a file
 line = ["\nWelcome to Python Programming", "\nPython is a great programming language", "\nPython is easy to learn"]
with open("sample.txt","a") as file:
    file.writelines(line)
    

## Read content from source file and write to destination file
with open("sample.txt",'r') as source_file:
    with open("destination.txt",'w') as destination_file:
        for line in source_file:
            destination_file.write(line)
            '''

## Read the text file and count the number of lines, words and characters in it
with open("sample.txt",'r') as file:
    content = file.read()
    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    print("Number of lines:", len(lines))
    print("Number of words:", len(words))
    print("Number of characters:", characters)