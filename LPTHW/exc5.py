name = 'Duy'
age = 23
height = round(1.65) #Meter
weight = 55 #kg
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

weight_pounds = weight*1.5

print(f"Let's talk about {name}.")
print(f"He's {height} meters tall")
print(f"He's {weight} kg heavy")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line ist tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")