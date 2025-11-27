
n=int(input("Enter the number: ")) 
       
rev=0
temp=n

while temp > 0:
    rev=rev<<1
    rev = rev | (temp&1)
    temp = temp>>1

print("reversed number is", rev)    