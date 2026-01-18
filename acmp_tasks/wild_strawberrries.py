berries = input()
berries_list = berries.split()
X = int(berries_list[0])
Y = int(berries_list[1])
Z = int(berries_list[2])

sum = X + Y
remaining_berries = sum - Z

if remaining_berries < sum:
    print(remaining_berries)
else:
    print("Impossible")