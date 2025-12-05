def power(n):
    if n <= 0:
        return False
    if n &(n-1) != 0:
        return False
    
    count = 0
    while(n&1) == 0:
        n>>= 1
        count+=1
    return ((count%3) == 0)

n=int(input("Enter the number: "))   

if power(n):
    print("it is a power of 8")
else:
   print("it is not a power of 8") 
