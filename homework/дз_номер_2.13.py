number = int( input("Введите трехзначное число: "))

if 100 <= number <= 999:

   digit1 = number // 100
   digit2 = (number // 10) % 10
   digit3 = number % 10

reversed_number = digit3 * 100 + digit2 * 10 + digit1

print(f"Число справа налево: {reversed_number}")

