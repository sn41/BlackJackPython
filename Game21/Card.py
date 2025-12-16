class Card:

    # конструктор
    def __init__(self, card_suit, card_rank, card_points):
        self._suit = card_suit
        self._rank = card_rank
        self.points = card_points

    def draw(self):
        d = self._rank
        m = self._suit
        print("┌────┐")
        print("│" + d + " " + m + "│")
        print("│    │")
        print("│ " + m + "  │")
        print("│    │")
        print("│" + m + " " + d + "│")
        print("└────┘")
