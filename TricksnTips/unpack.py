items = (1,2)
print(items)
print()

a, _ = (1,2)  #_ is for unused variables
print(a)
#print(b)

""" a , b, c = (1,2,3,4,5)

print(a) """
# error because too much values to unpack

a , b, *c = (1,2,3,4,5)
print(a)
print(b)
print(c)
print()
a, b, *c, d = (1,2,3,4,5,6,7,8,9)

print(a)
print(b)
print(c) # item 
print(d) # last item