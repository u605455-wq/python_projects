# польз вводит символ и программа должна определить буква ли это
# если это не буква программа должна определить цифра ли это
# если это не буква и не цифра то программа должна выдать что это неизвестный символ 

symbol_as_str = input("Введите символ: ")
symbol = symbol_as_str[0]

#print(ord(symbol))

if symbol >= 'a' and symbol <= 'z' or symbol >= 'A' and symbol <= 'Z':
    print("это английская буква!")

    if symbol >= 'a' and symbol <= 'z':
        print("маленькая")
    else:
        print("большая")

elif symbol >= '0' and symbol <= '9':
    print("это цифра!")
else:
    print("это неизвестный символ")

