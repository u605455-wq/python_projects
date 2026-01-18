

number = int( input("Введите четырехзначное число: "))
number1 = 0
number2 = 0
number3 = 0
number4 = 0
number_sum = 0


number1 = number // 1000 
number2 = (number // 100) % 10 
number3 = (number % 100) // 10
number4 = number % 10

number_sum = number1 + number2 + number3 + number4

print(f"Сумма:{number_sum}")
