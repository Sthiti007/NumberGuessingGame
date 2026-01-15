# NUMBER GUESSING GAME
# The user has to enter a number between 1 and 100, and according to the closeness of the inputed number to the number decided by the system,
# show weather it's "Too High" or "Too Low". The game stops when the user guesses the correct number.


import random

min_num = 1
max_num = 100
tries = 0

random_num = random.randint(min_num, max_num)

print("^^^^ NUMBER GUESSING GAME ^^^^")

while True:
    num = int(input(f"Enter a number between {min_num} & {max_num}: "))
    tries += 1

    if num < random_num:
        print("Low!")
    elif num > random_num:
        print("High!")
    else:
        print("CORRECT GUESS!")
        break

print(f"The answer is {random_num}.")
print(f"It took you {tries} tries to guess it!")

