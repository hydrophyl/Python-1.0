names = ['Cory','Chris', 'Dave', 'Trad']
heroes = ['Peru','Christie', 'David', 'Tradition']


""" for index, name in enumerate(names):
    hero = heroes[index]
    print(f"{name} is actually {hero}") """

for name, hero in zip(names,heroes):
    print(f'{name} is actually {hero}')

for value in zip(names,  heroes):
    print(value)