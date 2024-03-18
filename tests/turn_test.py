import pytest
from lib.card import Card
from lib.turn import Turn

def test_turn_init():
    card1 = Card('What is the capital of Alaska?', 'Juneau', 'Geography')
    turn1 = Turn('Juneau', card1)
    assert turn1.guess == 'Juneau'
    assert turn1.card == card1

def test_check_guess():
    card1 = Card('What is the capital of Alaska?', 'Juneau', 'Geography')
    
    # Correct answers
    turn1 = Turn('Juneau', card1)
    assert turn1.correct == True

    # Incorrect answers
    turn2 = Turn('Jo mama', card1)
    assert turn2.correct == False

def test_feedback():
    card1 = Card('What is the capital of Alaska?', 'Juneau', 'Geography')
    
    # Correct answers
    turn1 = Turn('Juneau', card1)
    assert turn1.feedback == "Correct!"

    # Incorrect answers
    turn2 = Turn('Jo mama', card1)
    assert turn2.feedback == "Incorrect."