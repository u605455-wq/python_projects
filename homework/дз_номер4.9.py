import math

number1 = float(input("Введите скорость в километрах в час: ")) #50
number2 = float(input("Введите скорость в метрах в секунду: ")) #43

number1 = number1 * 1
number2 = number2 * 1000 // 3600

if number1 > number2:
    print(f"Скорость в километрах в час больше, чем в метрах в секунду")
elif number1 < number2:
    print(f"Скорость в метрах в секунду больше, чем в километрах в час")
else:
    print(f"Они равны")