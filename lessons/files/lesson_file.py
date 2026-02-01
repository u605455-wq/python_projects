#file = open("hello_world.txt", "w", encoding="utf-8")

#file.write("Здравствуй, мир!")

#file.close()

file = open("input_15_8.txt", "r", encoding="utf-8")

file_data = file.read()


count_simbols = len(file_data)

file.close()

print(f"Количество символов - {count_simbols}")
#trtrtrtrtr

