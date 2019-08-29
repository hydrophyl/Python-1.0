#Asking questions
print("How old are you? ", end='')
age = input()
print("How tall are you? ", end='')
height = float(input())
print("How much do you weigh? ", end='')
weigh = float(input())
BMI_Wert = height / weigh
print(f"So, youre {age} old, {height} tall and {weigh} heavy.")
print(f"Your BMI ist: {BMI_Wert} ")


x = input('Enter your name: ')
print("Hello, ",x)