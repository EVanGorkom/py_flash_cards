class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.count = len(cards)

    def cards_in_category(self, category):
        match_count = 0
        for card in self.cards:
            if category == card.category:
                match_count += 1
        return match_count