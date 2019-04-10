class Person():
    pass

person = Person()

first_key = 'first'
first_val = 'Carey'

setattr(person, first_key, first_val)

""" person.first_key = first_val """

first = getattr(person, first_key)

print(first)
print()

person_info = {'first': 'Corey', 'last':'Schafer'}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))

