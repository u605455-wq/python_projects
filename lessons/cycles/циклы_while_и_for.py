# цикл while
# известно количество шагов
#i = 0
#N = 100
#sum_dist = 0
#dist_from_home = 0

#while i < N:
#    i = i + 1

#    current_step_dist = 1 / i
#    sum_dist = sum_dist + current_stop_dist

#    if i % 2 != 0:
#        dist_from_home = dist_from_home + current_stop_dist
#    else:
#        dist_from_home = dist_from_home - current_stop_dist

#print(f"Суммарная дистанция: {sum_dist:.3f} км") 
#print(f" дистанция от дома: {dist_from_home:.3f} км")
# НЕ известно количество шагов
#import math

#number = -1

#while number <= 0:
#    number = float(input("Введите число для извлечения квадратного корня: "))

#    if number <= 0:
#        print("Вы ввели число меньше или равно 0.Это неверно")
    
#result = math.sqrt(number)

#print(f"квадрвтный корень из числа {number} = {result:.2f}")


#distance = 10

#max_dist = 100

#current_day = 1

#while distance < max_dist:
#    distance = distance + distance * 0.1
#    current_day = current_day + 1

#    print(f"день №{current_day} дистанция = {distance:.1f} км")


# цикл for
#for _ in range(20):
#    print("20", end =" ")


#for i in range(1, 9 + 1):
#    print(f"{i} x 7 = {i*7}")


#a = int(input("введите а: "))

#b = a - 1

#while b < a:
#    b = int(input("введите b: "))
    
#    if b < a:
#       print("ошибка, b должно быть больше или равно a")

#sum = 0

#for i in range(a, b + 1):
#    sum = sum + i

#print(f"сума чисел от {a} до {b} = {sum}")


#distance = 10

#sum = distance

#for curent_day in range(2, 10 +1):
#    distance = distance + distance * 0.1
#    print(f"день №{curent_day} дистанция = {distance:.1f} км")

#    if curent_day <= 7:
#        sum = sum + distance

#print(f"за 7 дней суммарная дистанция = {sum:.1f} км")