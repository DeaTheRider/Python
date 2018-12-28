# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
b = [random.randint(0,9) for x in range(25)]
def square(list):
    a = list
    b = []
    for i in a:
        c = i**2
        b.append(c)
    return b
print(b)
print(square(b))


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
a = ["яблоко ","груша", "ананас ", "банан ","инжир "]
b = ["ананас ","виноград", "банан ","слива","инжир "]
c = list(set(a) & set(b))
c = [x for x in a if x in b]
print(c)



# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random

a = [random.randint(-100000,10000000) for x in range(10)]
c = []
b = [x for x in a if x > 0 and x % 3 == 0 and x% 4 != 0]
for i in a :
    if i > 0 and i % 3 == 0 and i% 4 != 0:
        c.append(i)
print(a)
print(c)
print(b)


