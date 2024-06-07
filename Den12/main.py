import random
import art
print(art.logo)
number = random.randint(1, 101)
have_won = False
number_of_quesses = 0
mode = input("Do you want to play easy mode or hard? ")
if mode == "easy":
    number_of_quesses = 10
elif mode == "hard":
    number_of_quesses = 5
while  have_won == False and number_of_quesses > 0:
    quess = int(input("Welcome to quess number. Guess number from 1 to 100."))
    if number == quess:
        print(f"You guessed the correct number. The number was {number}. ")
        have_won = True
    elif number < quess:
        print("Too high.")
        number_of_quesses -= 1
        print(f"You have {number_of_quesses} guesses left.")
    elif number > quess:
        print("Too low.")
        number_of_quesses -= 1
        print(f"You have {number_of_quesses} guesses left.")
    elif number_of_quesses >= 0:
        print(f"You failed the correct number was {number}")
        break

print("Game over!")


