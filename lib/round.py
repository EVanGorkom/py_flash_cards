from lib.turn import Turn
import pdb

class Round:
    def __init__(self, deck):
        self.deck = deck
        self.turns = []
        self.card_index = 0
        self.current_card = self.deck.cards[self.card_index]
        self.number_correct = 0
        # self.percent_correct = 0

    def take_turn(self, guess):
        turn = Turn(guess, self.current_card)
        if guess == self.current_card.answer:
            self.number_correct += 1
        self.turns.append(turn)
        self.card_index += 1
        return turn

    # def calc_percent_correct(self):
    #     # pdb.set_trace()
    #     if len(self.turns) == 0:
    #         return 0
    #     else:
    #         return (self.number_correct) / (len(self.turns)) * 100

    def number_correct_by_category(self, category):
        num_correct_by_cat = 0
        for turn in self.turns:
            if turn.card.category == category:
                num_correct_by_cat += 1
        return num_correct_by_cat

    def percent_correct_by_category(self, category):
        num = ((self.number_correct_by_category(category) / len(self.turns)) * 100)
        return float(num)
