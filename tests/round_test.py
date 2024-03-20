import pytest
from lib.card import Card
from lib.deck import Deck
from lib.turn import Turn
from lib.round import Round

def test_round_init():
    card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    deck = Deck([card1, card2, card3])
    round = Round(deck)
    new_turn = round.take_turn

    assert round.deck == deck
    assert round.current_card == card1

def test_take_turn_happy():
    card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    deck = Deck([card1, card2, card3])
    round = Round(deck)

    assert round.turns == []
    new_turn = round.take_turn("Juneau")

    assert new_turn.__class__ == Turn
    assert new_turn.correct == True
    assert round.turns == [new_turn]
    assert round.card_index == 1
    assert round.number_correct == 1
    assert round.percent_correct == 100.00

def test_take_turn_sad():
    card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    deck = Deck([card1, card2, card3])
    round = Round(deck)

    assert round.turns == []
    new_turn = round.take_turn("Jo mama")

    assert new_turn.__class__ == Turn
    assert new_turn.correct == False
    assert round.turns == [new_turn]
    assert round.card_index == 1
    assert round.number_correct == 0
    assert round.percent_correct == 0.00

def test_number_correct_by_category():
    card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    deck = Deck([card1, card2, card3])
    round = Round(deck)
    new_turn = round.take_turn("Juneau")

    assert round.number_correct_by_category("Geography") == 1

def test_percent_correct_by_category():
    card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    deck = Deck([card1, card2, card3])
    round = Round(deck)
    new_turn = round.take_turn("Juneau")

    assert round.percent_correct_by_category('Geography') == 100.00
    turn2 = round.take_turn("Jupiter")
    assert round.percent_correct_by_category('STEM') == 0.00
