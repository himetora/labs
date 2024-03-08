import os
#1
path = input("Enter the path: ")
print("\nDirectories and files:")
for dir in os.listdir(path):
    print(dir)
print("\nFiles:")
for entry in os.listdir(path):
    full_path = os.path.join(path, entry)
    if os.path.isfile(full_path):
        print(entry)
print("\nDirectories:")
for entry in os.listdir(path):
    full_path = os.path.join(path, entry)
    if os.path.isdir(full_path):
        print(entry)

#2
path = input("Enter the path: ")
def access(path):
    if(os.path.exists(path)):
        print("Directori exists")
    else:
        print("The specified path was not found.")

    if os.access(path, os.R_OK):
        print("The path is readable.")
    else:
        print("The path is not readable.")
    
    if os.access(path, os.W_OK):
        print("The path is writable.")
    else:
        print("The path is not writable.")

    if os.access(path, os.X_OK):
        print("The path is executable.")
    else:
        print("The path is not executable.")
access(path)

#3
path = input("Enter the path to check: ")
def check(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        directory, filename = os.path.split(path)
        print(f"Directory part: {directory}")
        print(f"Filename part: {filename}")
    else:
        print(f"The path '{path}' does not exist.")
check(path)

#4
filename = input("Enter the filename: ")
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print("File not found.")
        return None
counter = count_lines(filename)
print(counter)

#5
mylist = ['Itsuka', 'Furina', 'Cursed', 'Diablo']

with open('my_list.txt', 'w') as file:
    for item in mylist:
        file.write(item + '\n')

#6
for i in range(65, 91): 
    filename = chr(i) + '.txt'
    with open(filename, 'w') as file:
        file.write(f"This is the file for letter {chr(i)}.")

#7
with open('origin.txt', 'r') as origin_file:
    with open('copy.txt', 'w') as copy_file:
        content = origin_file.read()
        copy_file.write(content)

#8
path = input("path: ")
def check(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            try:
                os.remove(path)
                print(f"The file '{path}' has been successfully deleted.")
            except Exception as e:
                print(f"The file '{path}' could not be deleted. Error: {e}")
        else:
            print(f"There is no access to delete the file '{path}'.")
    else:
        print(f"File '{path}' does not exists.")
check(path)
