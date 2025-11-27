num = int(input("Enter a number: "))

temp = num
power = 0

while temp > 0:
    temp //= 10
    power += 1

temp = num
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** power
    temp //= 10

if armstrong_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")