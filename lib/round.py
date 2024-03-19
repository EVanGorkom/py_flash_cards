from lib.turn import Turn
import pdb

class Round:
    def __init__(self, deck):
        self.deck = deck
        self.turns = []
        self.card_index = 0
        self.current_card = self.deck.cards[self.card_index]
        self.number_correct = 0

    def take_turn(self, guess):
        turn = Turn(guess, self.current_card)
        if guess == self.current_card.answer:
            self.number_correct += 1
        self.turns.append(turn)
        self.card_index += 1
        return turn
    
