number = int(input("введите число: ")) # 9099
number_0 = 0
number_9 = 0

while number > 0:
    digit = number % 10
    number //= 10

    if digit == 0:
        number_0 = number_0 + 1
    if digit == 9:
        number_9 = number_9 + 1

if number_0 < number_9:
    print(f"количество 9 больше, чем 0.количество 9 = {number_9}, количество 0 = {number_0}")
elif number_0 > number_9:
    print(f"количество 0 больше, чем 9.количество 0 = {number_0}, количество 9 = {number_9}")
else:
    print(f"количество 0 и 9 одинаковое")