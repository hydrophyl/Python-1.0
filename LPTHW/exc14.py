""" from sys import argv

script, user_name = argv
prompt = '>.< '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f""""""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice. 
"""

from sys import argv

script, user_name = argv
prompt = '>,< >.< '

print(f"Hi {user_name}, I'm the {script} script.")
print("Now i have you ask you some questions.")
print("What's your girlfriends name? ")
girlfriend = input(prompt)

print("Where do you live?")
live = input(prompt)

print("How old are you?")
old = input(prompt)

print(f"""Alright you're {user_name} and your girlfriend is {girlfriend}.
You are living in {live} and you're {old} years old. Nice!!!""")