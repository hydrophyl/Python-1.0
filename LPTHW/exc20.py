from sys import argv

script, input_file = argv 

def print_all(file):
    print(file.read())

def rewind(file):
    file.seek(0)

def print_a_line(line_count, file):
    print(line_count, file.readline())

current_file = open(input_file)
total_line = sum(1 for line in current_file)
rewind(current_file)
print("First let's print the whole file: \n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print all lines from the beginning:")
current_line = 1
while(current_line <= total_line):
    print_a_line(current_line, current_file)
    current_line+= 1