money = input()
money_list = money.split()
a = int(money_list[0])
b = int(money_list[1])
c = int(money_list[2])

min_money = a

if b < min_money:
    min_money = b
if c < min_money:
    min_money = c

max_money = a

if b > max_money:
    max_money = b
if c > max_money:
    max_money = c

range = max_money - min_money

print(range)

