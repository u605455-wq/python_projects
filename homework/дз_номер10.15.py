def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("Простые трехзначные числа:")
for x in range(100, 1000):
    if is_prime(x):
        print(x)

