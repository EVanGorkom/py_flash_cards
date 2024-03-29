import requests
import pdb
from lib.card import Card
from lib.deck import Deck
from lib.turn import Turn
from lib.round import Round

def set_round_settings():
    categories = ["music", "history", "science", "geography"]
    while True:
        print("\n")
        category = input("What category, if any, do you want to focus on?\n(Leave blank if no preference)\n")
        if category in categories or category == '':
            break
    
    difficulties = ["easy", "medium", "hard"]
    while True:
        print("\n")
        difficulty = input("What difficulty would you like to play on? \nPlease enter either 'easy', 'medium', or 'hard'\n")
        if difficulty in difficulties or difficulty == '':
            break

    # API call
    BASE_URL = "https://the-trivia-api.com/v2/questions"
    request_url = f"{BASE_URL}?categories={category}?difficulties={difficulty}"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        print("\n")
        print("Quiz settings successfully updated!")
        return data
    else:
        print("\n")
        print("An error has occurred creating your quiz.\nPlease try again.")
        set_round_settings()

def populate_cards(api_data):
    cards = []
    for card_data in api_data:
        # pdb.set_trace()
        card = Card(card_data['question']['text'], card_data['correctAnswer'], card_data['category'])
        cards.append(card)
    return cards

# Intro logic
print("Welcome to Trivia Flash!")
print("\n")

running = False

while True:
    play_or_exit = input("Would you like to play? (y/n)\n")
    if play_or_exit == 'y':
        running = True
        break
    elif play_or_exit == 'n':
        print("Goodbye!")
        break
    else:
        print("Please enter either 'y' or 'n'.")

# Game logic
while running:
    # Initialize game settings
    data = set_round_settings()

    # Populate game objects
    cards = populate_cards(data)
    deck = Deck(cards)
    round = Round(deck)
    question_count = 1

    # Play the game
    print("\n")
    print(f"Let's start, you're playing with {len(cards)} cards.\n")
    print("-----------------S-T-A-R-T-!-----------------\n")

    while question_count <= len(cards):
        print(f"Question {question_count}: {round.current_card.question}")
        turn = round.take_turn(input(""))
        if turn.correct:
            print(turn.feedback)
            print('\n')
        else:
            print(turn.feedback)
            print(f"The correct answer was: {turn.card.answer}")
            print('\n')
        question_count += 1
    
    print("ROUND OVER!!!\n")
    print("---------------R-E-S-U-L-T-S---------------\n")
    print(f"Your percent correct was: {round.percent_correct}")
    if round.percent_correct < 70.0:
        print("I'm sure you'll smash it next time!")
    elif round.percent_correct >= 70.0:
        print("Well done!")
    elif round.percent_correct >= 90.0:
        print("Very impressive!")

    while True:
        play_again = input("\nWould you like to play again? (y/n)\n")
        if play_again.lower() == 'y':
            break
        elif play_again.lower() == 'n':
            print("\nGame Over, thanks for playing!")
            running = False
            break
        else:
            print("Please enter either 'y' or 'n'.")

