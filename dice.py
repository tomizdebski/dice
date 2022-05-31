"""
Kostka do gry
Warsztat: Kostka do gry

W grach planszowych i papierowych RPG używa się wielu rodzajów kostek do gry, nie tylko tych dobrze znanych, sześciennych.
Jedną z popularniejszych kości jest np. kostka dziesięciościenna, a nawet stuścienna!
Ponieważ w grach kośćmi rzuca się często, pisanie za każdym razem np.
"Rzuć dwiema kostkami dziesięciościennymi, a do wyniku dodaj 20" byłoby nudne, trudne i marnowałoby ogromne ilości papieru.
 W takich sytuacjach używa się kodu "rzuć 2D10+20".

Kod takiej kostki wygląda następująco:

xDy+z
gdzie:

y – rodzaj kostek, których należy użyć (np. D6, D10),
x – liczba rzutów kośćmi; jeśli rzucamy raz, ten parametr jest pomijalny,
z – liczba, którą należy dodać (lub odjąć) do wyniku rzutów (opcjonalnie).
Przykłady:

2D10+10: 2 rzuty D10, do wyniku dodaj 10,
D6: zwykły rzut kostką sześcienną,
2D3: rzut dwiema kostkami trójściennymi,
D12-1: rzut kością D12, od wyniku odejmij 1.
Napisz funkcję, która:

przyjmie w parametrze taki kod w postaci łańcucha znaków,
rozpozna wszystkie dane wejściowe:
rodzaj kostki,
liczbę rzutów,
modyfikator,
jeśli podany ciąg znaków jest niepoprawny, zwróci odpowiedni komunikat,
wykona symulację rzutów i zwróci wynik.
Typy kostek występujące w grach: D3, D4, D6, D8, D10, D12, D20, D100.
"""
import random

DICES = ('D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100')

print("""
Masz do wyboru takie kostki:
D3, D4, D6, D8, D10, D12, D20, D100
Kod takiej kostki wygląda następująco:

xDy+z
gdzie:

y – rodzaj kostek, których należy użyć (np. D6, D10),
x – liczba rzutów kośćmi; jeśli rzucamy raz, ten parametr jest pomijalny,
z – liczba, którą należy dodać (lub odjąć) do wyniku rzutów (opcjonalnie).

""")


def throw_a_dice(input_dice):
    """
    The player rolls the dice
    :param input_dice: str  the function takes the dice roll code
    :return: int score
    """
    for dice in DICES:
        if dice in input_dice:
            multiply, modifier = input_dice.split(dice)
            dice_value = int(dice[1:])
            if multiply:
                multiply = int(multiply)
            else:
                multiply = 0
            if modifier:
                modifier = int(modifier)
            else:
                modifier = 0
    score = sum([random.randint(1, dice_value) for i in range(multiply)]) + modifier
    return score


if __name__ == '__main__':
    print(throw_a_dice('2D10+10'))
