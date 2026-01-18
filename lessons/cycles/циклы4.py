a = 1
b = 1
c = 1

while a <= 50:
    while b <= 50:
        while c <= 50:
            if c * c == a * a + b * b:
                print(f"a = {a} b = {b} c = {c}")
            c = c + 1
        c = 1
        b = b + 1
    b = 1
    a = a = 1