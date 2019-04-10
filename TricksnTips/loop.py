names = ['Cory','Chris', 'Dave', 'Trad']

""" index = 0 

for name in names:
    print(index, name)
    index += 1 """

for index, name in enumerate(names, start = 1):
    print(index, name)