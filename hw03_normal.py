# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a = [1, 1]
    c = 0
    while len(a) < m:
        b = a[0+c] + a[1+c]
        a.append(b)
        c = c + 1

    return a[n:m+1]
    pass
print(fibonacci(1, 12))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    l = origin_list
    n = 1
    while n < len(l):
        for i in range(len(l) - n):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
        n = n + 1
    return l


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])




# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(f, l):
    result_l = []

    for item in l:
        if f(item):
            result_l.append(item)

    return result_l


print(my_filter(lambda x: x > 100, [100, 200, 50, 150]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def qwe (A1,A2,A3,A4):
    x1, y1 = A1
    x2, y2 = A2
    x3, y3 = A3
    x4, y4 = A4
    a = "Это параллелограмм"
    if (x2 - x1) == (x4-x1) and (y2 - x1) == (y2 - y1):
        return a
    elif (x2 - x1) == (x3 - x4) and (y2 - y1) == (y3 - y4):
        return a
    elif (x2 - x1) == (x4 - x2) and (y2 - y1) == (y4 - y2):
        return a
    elif (x2 - x1) == (x2 - x4) and (y2 - y1) == (y2 - y4):
        return a
    elif (x2 - x1) == (x2 - x3) and (y2 - y1) == (y2 - y3):
        return a
    elif (x2 - x1) == (x3 - x2) and (y2 - y1) == (y3 - y2):
        return a
    else:
        a = "Это не параллелограмм"
        return a
print(qwe(A1 = (8,-3), A2 = (2,5), A3 = (10,11), A4 = (16, 3) ))
print(qwe(A1 = (8,-5), A2 = (4,5), A3 = (11,11), A4 = (16, 5) ))

