a = print(int(input("введите число: ")))

if a == 0:
    min_digit = 0
    max_digit = 0
else:
    min_digit = 9
    max_digit = 0

    temp = a

    while temp > 0:
        digit = temp % 10

        if digit < min_digit:
            min_digit = digit
        if digit > max_digit:
            max_digit = digit

        temp = temp // 10

print(f"минимальная цифра = {min_digit}")
print(f"максимальная цифра = {max_digit} ")

