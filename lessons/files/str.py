file = open("strok.txt", "r", encoding='utf-8')

line_count = 0
for line in file:
    line_count += 1

file.close()

file_out = open("ressult.txt", "w", encoding='utf-8')
file_out.write(f"Количество строк - {line_count}")

file_out.close()

