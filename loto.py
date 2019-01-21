#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random
l = [i for i in range(1,90)]
l2 = l[:]
l3 = l[:]


class Card(list):
    def __init__(self,l):
        self.l = l[:]
    def first_str(self):
        l1 = []
        while True:
            if len(l1) < 5:
                el = random.choice(l)
                l1.append(el)
                l.remove(el)
            elif len(l1) < 9:
                l1.append(None)
            else:
                break
        random.shuffle(l1)
        return l1
    def second_str(self):
        l2 = []
        while True:
            if len(l2) < 5:
                el = random.choice(l)
                l2.append(el)
                l.remove(el)
            elif len(l2) < 9:
                l2.append(None)
            else:
                break
        random.shuffle(l2)
        return l2
    def thri_str(self):
        l3 = []
        while True:
            if len(l3) < 5:
                el = random.choice(l)
                l3.append(el)
                l.remove(el)
            elif len(l3) < 9:
                l3.append(None)
            else:
                break
        random.shuffle(l3)

        return l3

Com = [Card.first_str(l),Card.second_str(l),Card.thri_str(l)]
Player = [Card.first_str(l2),Card.second_str(l2),Card.thri_str(l2)]

def choice(l):
    el = random.choice(l)
    l.remove(el)
    return el

def my_print(l):
    for i in l:
        print(i)

def change_element(l, b):
    for row in l:
        for i, val in enumerate(row):
            if val == b:
                row[i] = '-'
    return l

def check_on_element(l, b):
    a = False
    for row in l:
        for i, val in enumerate(row):
            if val == b:
                row[i] = '-'
                a = True
    return a
def check_on_card(l):
    e = False
    for row in l:
        for i, val in enumerate(row):
            if type(val) == int:
                e = True
    return e




d = True

s = 0

while d :
    e = 0
    w = 0
    if check_on_card(Com) == False:
        print("Вы проиграли")
        d = False
        break
    elif check_on_card(Player) == False:
        print("Вы выиграли")
        d = False
        break

    print("Ваша карточка")
    my_print(Player)
    print("Карта соперника")
    my_print(Com)
    b = choice(l3)
    print("Бочонок с № {}, осталось {}".format(b,len(l3)))
    a = input("Если зачеркнуть нажмите 1, если продолжить нажмите 2 ")
    if a == "1":
        change_element(Com,b)

        if check_on_element(Player,b) == True:
            change_element(Player,b)

        else:
            d = False
            print("Вы проиграли")
            break

    elif a == "2":
        change_element(Com, b)

        if check_on_element(Player,b) == True:
            print("Вы проиграли")
