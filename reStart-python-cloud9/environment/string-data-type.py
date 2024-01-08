myString= "This is a string"
firstString= "Water"
secondString= "fail"
name=input("What is your name?")
color=input("What is your favorite color?")
animal=input("What is your favorite animal?")

print(myString)

print(str(myString) + " Is of the data type " + str(type(myString)))

print(firstString + secondString)

print(name)

print("{}, you like a {} {}!".format(name,color,animal))