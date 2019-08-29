from sys import argv

script, user_name = argv

prompt = 'message: '

print(f'Are you {user_name}?')
print(f'This is {script} script!')
print('Where do you live? ')
live = input(prompt)

print(f'So u live in {live}! And u are {user_name}!')