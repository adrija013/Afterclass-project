def reverse_bits(n):
    result = 0
    bit_length = n.bit_length()  

    for _ in range(bit_length):

        result <<= 1
 
        result |= (n & 1)

        n >>= 1

    return result

num = int(input("Enter a number: "))
reversed_num = reverse_bits(num)

print("Reversed-bit number:", reversed_num)