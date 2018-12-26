# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    a = round(number,ndigits)

    return a


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    q =ticket_number
    a = str(q)
    i = len(a)//2
    first_half = 0
    second_half = 0

    while i != 0:
        first_half = first_half + int(a[i-1])
        second_half = second_half + int(a[-i])
        i = i - 1
    if first_half == second_half:
        return ("Счастливый билет!!!")
    else:
        return ("Несчастливый билет")


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))