import os

# Поскольку теперь вы запускаете код как пакет, Python изменит то, как он ищет файлы Deck и Card.
# Старые импорты (from Deck import Deck) перестанут работать, так как эти файлы больше не находятся в "корне" поиска, они находятся внутри пакета Game21.
# Вам нужно изменить начало файла Game21/main.py, добавив точку перед именами модулей (относительный импорт):

# from Deck import Deck
# from Card import Card

# Точка означает "искать в этой же папке пакета"
from .Deck import Deck



def clear_screen():
    # в Window обычно достаточно:
    # os.system('cls' if os.name == 'nt' else 'clear')

    # В Linux и macOS не только нужно очищать видимую часть консоли, но и буфер прокрутки:
    # \033c сбрасывает состояние терминала, а \033[3J очищает буфер прокрутки.
    print("\033c\033[3J", end="")



def draw_card(deck):
    card = deck.get_card()
    points = card.points
    card.draw()
    return points


# todo Добавьте очистку экрана перед каждым показом карт
def game():
    deck = Deck()
    total = 0
    card_points = draw_card(deck)
    total = total + card_points
    while True:
        card_points = draw_card(deck)
        total = total + card_points
        if total < 21:
            print(f"ВЫ НАБРАЛИ {total} ОЧКОВ!  \n ЕЩЁ ?")
            input_first_char = input().lower()[0]
            if input_first_char != "y":
                break

        else:
            break

    clear_screen()

    if total == 21:
        print("ВЫИГРЫШ!")
    elif total > 21:
        print("ПЕРЕБОР!")
    else:
        print(f"У ВАС {total} ОЧКОВ!")


if __name__ == '__main__':
    game()


