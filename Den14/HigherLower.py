import random
import art
import data

def format_data(account):
    print(f"{account["name"]} a {account["description"]} from {account["country"]}")
def chech_answer(guess, a_followers, b_followers):
    if guess == "a":
        return a_followers > b_followers
    else:
        return a_followers < b_followers
def game():
  print(art.logo)
  global score
  score = 0

print(art.logo)

score = 0
game_should_continue = True
account_a = random.choice(data.data)
account_b = random.choice(data.data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data.data)
    while account_a == account_b:
        account_b = random.choice(data.data)

    format_data(account_a)
    print(art.vs)
    format_data(account_b)
    print("\n")
    guess = input("Who has more followers A or B? ").lower()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_correct = chech_answer(guess, a_followers, b_followers)
    if chech_answer(guess, a_followers, b_followers):
        score += 1
        print(f"Correct! Your score is {score}")
    else:
        print(f"Incorrect! Your final score is {score}")
        should_continue = input("Would you like to play again? Type yes or no").lower()
        if should_continue == "no":
            game_should_continue = False
        else:
            game()