print("How old are you? ", end='')
age = input()
print("How tall are you? ", end='')
height = int(input())
print("How much do you weigh? ", end='')
weigh = int(input())
BMI_Wert = height / weigh
print(f"So, youre {age} old, {height} tall and {weigh} heavy.")
print(f"Your BMI ist: {BMI_Wert} ")