start_number = int(input("Введите стартовое число: "))
finish_number = int(input("Введите конечное число: "))
step = int(input("Введите шаг приращения: "))

#i = start_number

#while i <= finish_number:
#    print(i, end =" ")
#    i = i + step
    
i = finish_number

while i >= start_number:
    print(i, end =" ")
    i = i - step
