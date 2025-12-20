
def setOrnot(n):
    pos = 1  

    while n > 0:
        if (n & 1) == 1: 
            return pos     
        n >>= 1            
        pos += 1

    return None            

number = int(input("Enter the number: "))
result = setOrnot(number)

if result is None:
    print("No set bits (number is 0).")
else:
    print("Position of rightmost set bit:", result)