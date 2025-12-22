def longest_consecutive_ones(n):
    max_count = 0
    count = 0
    while n > 0:
        n = n & (n << 1)
        count += 1
        if count > max_count:
            max_count = count
    return max_count
number = int(input("Enter a number: "))
print(f"Longest consecutive 1s: {longest_consecutive_ones(number)}")