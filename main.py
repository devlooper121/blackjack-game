
import random

def deal(cards):
    ''' This function take a list of card as argument and return a random card'''
    card = cards.pop()
    return card
player_cards = []
computer_cards = []

# def clear():
# 	if os.name == 'nt':
# 		os.system('CLS')
# 	if os.name == 'posix':
# 		os.system('clear')

# first draw


def calculate_score(cards):
    ''' This function take a list of card as argument and return sum of card point along with black jack = 0 and ace two value acording condition'''
    if sum(cards) == 21 and len(cards) ==2:
        return 0 
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player_score, computer_score):
    ''' This function take playerr score and computer score as argument and compare according blackjack rules'''
    if player_score == 0:
        print("Win with a Blackjack 😎")
    elif computer_score == 0:
        print("Lose, computer has Blackjack 😱")
    elif player_score > 21 and computer_score > 21:
        print("Busted. You lose 😭")
    elif player_score < 21 and computer_score > 21:
        print("computer Busted. You win 😁")
    elif player_score == computer_score:
        print("Draw 🙃")
    elif player_score > computer_score:
        print("You win 😃")
    else:
        print("You lose 😤")
# importin logo from art.py from same directory
from art import logo
print(logo)

def play():
    ''' This function takes no argument and run until player draw card and computer also '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
    random.shuffle(cards)
    player_cards = []
    computer_cards = []
    # first 2 draw
    for _ in range(2):
        player_cards.append(deal(cards))
        computer_cards.append(deal(cards))
    # while player draw card
    player_taking_cards = True

    while player_taking_cards:
        player_score =  calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Player card :{player_cards} and score = {player_score} ")
        print(f"    computer first card : {computer_cards[0]} ")
        # condition for drawing card
        if computer_score == 0 or player_score == 0 or player_score > 21:
            player_taking_cards = False
        
        else:
            hit = input("Do you want Another card ? 'y' or 'n' : ")
            if hit == "y":
                player_cards.append(deal(cards))
            else:
                player_taking_cards = False

    # computer_turn of drawing carrd until 17

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal(cards))
        computer_score = calculate_score(computer_cards)

    print(f"plyer has these cards : {player_cards} and score is {player_score}")
    print(f" Computer has these cards : {computer_cards} and score is {computer_score}")
    compare(player_score, computer_score)


# main funtion 
while input("You want to play game 'y' or 'n': " ).lower() == 'y':
    # clear()
    play()
    