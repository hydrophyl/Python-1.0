a = [1,5,7,8,9,4,2,3]

good = False
for index in range(len(a) - 1):
    if a[index] > a[index + 1]:
        good = True

while(good == True):
    for i in range (0,len(a) - 1 ):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]

for i in range (0,len(a) - 1):
    print(a[i])