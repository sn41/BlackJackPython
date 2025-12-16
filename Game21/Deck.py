import random

# from Card import Card
# Точка означает "искать в этой же папке пакета"
from .Card import Card


class Deck:
    # конструктор
    def __init__(self):
        self.exists = [True] * 36

    def get_random_id(self):
        while True:
            card_id = random.randint(0, 35)
            card_exists = self.exists[card_id]
            if card_exists:
                self.exists[card_id] = False
                return card_id

    # todo вынести получение масти, ранга и очков карты в отдельные функции
    def get_card(self):
        card_id = self.get_random_id()

        # todo исправить оператор обычного деления на оператор целочисленного деления
        card_suit_id = card_id // 9

        suit = ""
        rank = ""
        points = 0

        match card_suit_id:
            case 0:
                suit = "♠"
            case 1:
                suit = "♣"
            case 2:
                suit = "♦"
            case _:
                suit = "♥"

        # todo исправить оператор обычного деления на оператор получения остатка от деления
        card_rank_points_id = card_id % 9

        match card_rank_points_id:
            case 0:
                rank = " 6"
                points = 6
            case 1:
                rank = " 7"
                points = 7
            case 2:
                rank = " 8"
                points = 8
            case 3:
                rank = " 9"
                points = 9
            case 4:
                rank = "10"
                points = 10
            case 5:
                rank = " T"
                points = 1
            case 6:
                rank = " В"
                points = 2
            case 7:
                rank = " Д"
                points = 3
            case _:
                rank = " К"
                points = 4

        return Card(suit, rank, points)


