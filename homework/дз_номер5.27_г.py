a = float(input("введите число a: "))
b = float(input("введите число b(b >= a): "))

if b < a:
    print("Ошибка: b должно быть больше или равно a")
else:
    total = 0
    i = a
    while i <= b:
        total = total + i
        i = i + 1
    print(f"Сумма чисел от  a до b: {total}")
