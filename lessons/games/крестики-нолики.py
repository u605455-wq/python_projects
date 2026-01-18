import random

ZERO = "o"
CROSS = "x"
EMPTY_CELL = "."
user_choice = 0
comp_choice = 0
field = []

COLS = 3
ROWS = 3

for i in range(ROWS):
    field.append([])
    for j in range(COLS):
        field[i].append(EMPTY_CELL)

    
print("Добро пожаловать в игру крестики-нолики!")

while True:
    user_choice = input("Введите каким символом будете играть х или о: ")
    if user_choice == ZERO:
        comp_choice = CROSS
        break
    elif user_choice == CROSS:
        comp_choice = ZERO
        break
    else:
        user_choice = input("Неверный символ. Введите еще раз: ")
        if user_choice == ZERO:
            comp_choice = CROSS
            break
        elif user_choice == CROSS:
            comp_choice = ZERO
            break

print(f"Ваш выбор - {user_choice}. Приятной игры!")

User_step = "USER"
Comp_step = "COMP"
current_step = ""

FILLED_CELL_USER = user_choice
FILLED_CELL_COMP = comp_choice

print("Игровое поле: ")
if random.randint(1, 10) < 5:
    current_step = User_step
else:
    current_step = Comp_step

game_is_running = True

while game_is_running == True:
    for i in range(ROWS):
        for j in range(COLS):
            print(field[i][j], end="")
        print()

    if current_step == User_step:
        print("Ход человека:")
        i_input = int(input("введите номер строки: ")) -1
        j_input = int(input("введите номер столбца: ")) -1
        if field[i_input][j_input] == EMPTY_CELL:
            if i_input != (1, ROWS) and j_input != (1, COLS):
                print("Ошибка.Номер строки и номер столбца должны быть от 1 до 3")
            elif i_input == (1, ROWS) and j_input == (1, COLS):
                field[i_input][j_input] = FILLED_CELL_USER
                current_step = Comp_step

    elif current_step == Comp_step:
        print("Ход компьютера (нажмите Enter):")
        input()

        i_input = random.randint(0, ROWS -1)
        j_input = random.randint(0, COLS -1)

        if field[i_input][j_input] == EMPTY_CELL:
            field[i_input][j_input] = FILLED_CELL_COMP

        current_step = User_step