#PAUSE 1
# Fix the len() fn
# len(123456)
# As len does not accept int value, we change the input to string

print(len("123456"))

#PAUSE 2
# Generate data type using type() fn

print(type("Shaivi"))
print(type(12390))
print(type(3.14259))
print(type(True))

#Type Conversion

print("123" + "456")
print(int("123") + int("456"))

#PAUSE 3: Debug the code
# print("Number of letters in your name: " + len(input("Enter your name")))

name = input("Enter your name: ")
l = len(name)
print("Number of letters in your name: " + str(l))
print("Number of letters in your name: " + str(len(input("Enter your name"))))