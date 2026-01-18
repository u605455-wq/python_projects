num = int(input("введите трёхзначное число: "))

digit1 = num // 100
digit2 = ( num // 10 ) % 10
digit3 = num % 10

reversed_num = digit2 * 100 + digit3 * 10 + digit1
print(f"{reversed_num}")