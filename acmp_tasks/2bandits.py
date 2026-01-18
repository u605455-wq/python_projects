banks = input()
banks_list = banks.split()
Garry = int(banks_list[0])
Larry = int(banks_list[1])

Garry_banks = 10 - Garry
Larry_banks = 10 - Larry

print(f"{Garry_banks} {Larry_banks}")