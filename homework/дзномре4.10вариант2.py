a = float(input("Введите первое число: ")) #5
b = float(input("Введите второе число: ")) #8
c = float(input("Введите третье число: ")) #2

numbers = sorted([a, b, c])

minimum = numbers[0]
middle = numbers[1]
maximum = numbers[2]

print(f"Наибольшее число: {maximum}")
print(f"Наименьшее число: {minimum}")
print(f"Среднее число: {middle}")