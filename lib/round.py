from lib.turn import Turn
import pdb

class Round:
    def __init__(self, deck):
        self.deck = deck
        self.turns = []
        self.card_index = 0
        self.current_card = self.deck.cards[self.card_index]
        self.number_correct = 0
        self.percent_correct = 0.0

    def take_turn(self, guess):
        turn = Turn(guess, self.current_card)
        self.turns.append(turn)
        if guess == self.current_card.answer:
            self.number_correct += 1
        
        self.card_index += 1
        if self.card_index < len(self.deck.cards):
            self.current_card = self.deck.cards[self.card_index]

        self.calc_percent_correct()
        return turn

    def calc_percent_correct(self):
        if len(self.turns) == 0:
            self.percent_correct = 0.00
        else:
            self.percent_correct = float(self.number_correct / len(self.turns) * 100)

    def number_correct_by_category(self, category):
        num_correct_by_cat = 0
        for turn in self.turns:
            if turn.card.category == category:
                num_correct_by_cat += 1
        return num_correct_by_cat

    def percent_correct_by_category(self, category):
        num = ((self.number_correct_by_category(category) / len(self.turns)) * 100)
        return float(num)
        # This is not actually calculating properly. it's looking at all turns instead of turns of that category