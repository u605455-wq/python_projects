import math


radius = float(input("Введите радиус круга: "))
side = float(input("Введите сторону квадрата: "))

circle_perimeter = 2 * math.pi * radius
square_perimeter = side * 4

if circle_perimeter < square_perimeter:
    print("Квадрат больше, чем круг")
elif circle_perimeter > square_perimeter:
    print("Круг больше, чем квадрат")
else:
    print("Круг и квадрат равны")
