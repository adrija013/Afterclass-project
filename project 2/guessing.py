import random

numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))

chosen_number = random.choice(numbers)

guess = int(input("Guess the number chosen by the judge: "))


if guess > chosen_number:
    print("Your guessed number is HIGHER than the original number.")
elif guess < chosen_number:
    print("Your guessed number is SMALLER than the original number.")
else:
    print("Congratulations! You guessed the CORRECT number.")

print("Best of luck!")


