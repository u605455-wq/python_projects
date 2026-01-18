nuts = input()
nuts_list = nuts.split()
N = int(nuts_list[0])
M = int(nuts_list[1])
user_K = int(nuts_list[2])

K = N * M

if user_K <= K:
    print("YES")
else:
    print("NO")