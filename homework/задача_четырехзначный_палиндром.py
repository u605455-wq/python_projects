N = int(input("введите четырехзначное число: "))
if N > 9999:
    print("ошибка, число должно быть четырехзначным(меньше или равно 9999)")
if N <= 9999:
    digit1 = N // 1000
    digit2 = (N // 100) % 10
    digit3 = (N // 10) % 10
    digit4 = N % 10
    polindrom = digit4 * 1000 + digit3 * 100 + digit2 * 10 + digit1
    if polindrom == N:
        print("YES")
    else:
        print("NO")
