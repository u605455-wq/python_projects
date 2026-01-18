

number1 = int( input("Введите первое число: "))
number2 = int( input("Введите второе число: "))
number3 = int( input("Введите третье число: "))

max_number = max(number1, number2, number3)
min_number = min(number1, number2, number3)

if number1 != max_number and number1 != min_number:
    middle_number = number1
elif number2 != max_number and number2 != min_number:
    middle_number = number2
else:
    middle_number = number3

print(f"Наибольшее число: {max_number}")
print(f"Наименьшее число: {min_number}")
print(f"Среднее число: {middle_number}")

