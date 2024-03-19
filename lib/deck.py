class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.count = len(cards)

    def cards_in_category(self, category):
        match = []
        for card in self.cards:
            if category == card.category:
                match.append(card)
        return match