import math
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class Triangle(object):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3


    def perimetr(self):
        AB = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        AC = math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)
        CB = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        P = AB + AC + CB
        return P
    def area(self): #S = |(x1 – x3)·(y2 – y3) – (x2 – x3)·(y1 – y3)|/2
        S = ((self.x1 - self.x3)*(self.y2-self.y3) - (self.x2 - self.x3)*(self.y1-self.y3))/2
        if S <0:
            S = -S
        return S
    def height_1(self):
        CB = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        S = ((self.x1 - self.x3)*(self.y2-self.y3) - (self.x2 - self.x3)*(self.y1-self.y3))/2
        h1 = (S*2)/CB
        return h1




first_triangle = Triangle(7, -3, 5, 5, 3, -3) #(3, -3, 7, -3, 5, 5)
print(first_triangle.perimetr())
print(first_triangle.area())
print(first_triangle.height_1())
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class Trapezium(object):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.AB = math.sqrt((x2-x1)**2 +(y2-y1)**2)
        self.BC = math.sqrt((x3-x2)**2 +(y3-y2)**2)
        self.CD = math.sqrt((x4-x3)**2 +(y4-y3)**2)
        self.AD = math.sqrt((x4-x1)**2 +(y4-y1)**2)
        self.AC = math.sqrt((x3-x1)**2 +(y3-y1)**2) # диагональ 1
        self.BD = math.sqrt((x4-x2)**2 +(y4-y2)**2) # диагональ 2
    def check(self):
        if self.AC == self.BD :
            a = "Это Равнобедренная трапеция"

        else:
            a = "Это не равнобедренная трапеция"
        return a
    def perimetr(self):
        P = self.AB + self.BC + self.CD + self.AD
        return P
    def area(self):
        S = ((self.AD + self.BC)/2)* math.sqrt((self.BC)**2-((self.AD - self.BC)**2)/4)
        return S







first_trapezium = Trapezium(-6, 1, 0, 5, 6, -4, 0, -8)
print(first_trapezium.check())
print(first_trapezium.area())



