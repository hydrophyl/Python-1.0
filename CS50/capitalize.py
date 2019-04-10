from cs50 import get_string

s = get_string("Name: ")
for i in s:
    print(i.upper(), end = "")
print()