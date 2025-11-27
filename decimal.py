binary = input("enter a binary number: ")

decimal = 0
for digit in binary:
    decimal = (decimal<<1) | int(digit)

print("Decimal number: ",decimal)    