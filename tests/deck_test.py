import pytest
from lib.card import Card
from lib.deck import Deck

@pytest.fixture
def setup_deck():    
    card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    deck = Deck([card1, card2, card3])
    return deck

def test_deck_init(setup_deck):
    assert setup_deck.cards[0].question == "What is the capital of Alaska?"
    assert setup_deck.cards[1].question == "The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?"
    assert setup_deck.cards[2].question == "Describe in words the exact direction that is 697.5° clockwise from due north?"
    assert setup_deck.cards[0].answer == "Juneau"
    assert setup_deck.cards[1].answer == "Mars"
    assert setup_deck.cards[2].answer == "North north west"
    assert setup_deck.cards[0].category == "Geography"
    assert setup_deck.cards[1].category == "STEM"
    assert setup_deck.cards[2].category == "STEM"
    assert setup_deck.count == 3

def test_cards_in_category(setup_deck):
    assert setup_deck.cards_in_category("STEM") == 2
    assert setup_deck.cards_in_category("Geography") == 1