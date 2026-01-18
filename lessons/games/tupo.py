import random

comp_number = random.randint(1,100)
user_number = 0
is_guess = False

print("Я загадал число от 1 до 100. Попробуй отгадать")

while is_guess == False:
    user_number = int(input("Введите свое число: "))

    if user_number > comp_number:
        print("введите поменьше")
    elif user_number < comp_number:
        print("введите побольше")
    else:
        print("Урааа вы победили!!!!!!!!!")
        ise_guess = True