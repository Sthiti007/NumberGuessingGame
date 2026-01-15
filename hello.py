# NUMBER GUESSING GAME 


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
