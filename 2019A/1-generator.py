import random


n = 100000
p = [1, 3, 10, 30, 50, 70, 100, 300, 500, 1000, 5000, 8000, 10000, 30000, 50000, 70000, 100000]
print(len(p))
for x in p:
    print(n, x)
    print(" ".join([str(int(random.random() * 10000)) for i in range(n)]))
