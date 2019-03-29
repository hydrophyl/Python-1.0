import datetime
now = datetime.datetime.now()

name = input("Hey what's your name: ")
age = int(input("Ok {}, What's your age: ".format(name.title())))

yrs = (now.year + 100) -age

msg = ("Ok {}, so you're {} years old and the year {} hat your 100th birthday!\n".format(name.title(),age,yrs))
print(msg)