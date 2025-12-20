a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

temp = a
a = b
b = c
c = temp


print("After swapping:")
print("a =", a)
print("b =", b)
print("c =", c)