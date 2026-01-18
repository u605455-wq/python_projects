import random

a = [random.randint(2, 5) for _ in range(10)]

print(f"случайные оценки ученика:{a}")

count_4 = 0
count_5 = 0

for i in a:
    if i == 4:
        count_4 = count_4 + 1
    if i == 5:
        count_5 = count_5 + 1

total = count_5 + count_4

print(f"четверки = {count_4}, пятерки = {count_5}, всего = {total}")

