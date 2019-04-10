n = int(input("Please give me a number: "))

if n % 4 == 0:    
    print("THis number is by 4 divided!")
elif n%2 == 0:
    print("THis number is an even number!")
else:
    print("This number is an odd number!")

num = float(input("checked number: "))
check = float(input("number to divided by: "))
if num % check == 0:
    print("{} is divided by {}".format(num, check))
else:
    print("An appropriate message!")
print("*" *30)