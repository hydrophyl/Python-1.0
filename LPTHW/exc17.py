from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")
open(to_file).write(open(from_file).read())
out_file.close()
