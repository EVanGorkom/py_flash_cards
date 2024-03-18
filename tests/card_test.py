import pytest
# from lib import card
from lib.card import Card

def test_card_init():
    card1 = Card('What is the capital of Alaska?', 'Juneau', 'Geography')
    assert card1.question == 'What is the capital of Alaska?'
    assert card1.answer == 'Juneau'
    assert card1.category == 'Geography'