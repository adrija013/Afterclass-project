def print_substrings(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            print(s[i:j])

string = input("Enter a string: ")
print_substrings(string)