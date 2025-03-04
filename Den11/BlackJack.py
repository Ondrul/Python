import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def is_already_win(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return True
    return False


def calculate_score(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose."
    if user_score == computer_score:
        return "Draw "
    elif user_score > 21:
        return "You went over. You lose "
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win "
    else:
        return "You lose "


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    has_user_black_jack = False
    has_computer_black_jack = False
    while not is_game_over:
        has_user_black_jack = is_already_win(user_cards)
        has_computer_black_jack = is_already_win(computer_cards)
        if has_user_black_jack or has_computer_black_jack:
            break

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type yes to get another card, type no to pass: ")
            if user_should_deal == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    if not has_user_black_jack and not has_computer_black_jack:
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    user_already_won = has_user_black_jack
    computer_already_won = has_computer_black_jack



    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type yes or no: ") == "yes":
    play_game()
