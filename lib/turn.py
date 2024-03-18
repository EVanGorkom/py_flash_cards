class Turn:
    def __init__(self, guess, card):
        self.guess = guess
        self.card = card
        self.correct = self.check_guess()
        self.feedback = self.response()

    def check_guess(self):
        return self.guess == self.card.answer

    def response(self):
        if self.correct == True:
            return "Correct!"
        else:
            return "Incorrect."