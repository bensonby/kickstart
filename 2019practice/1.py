import math

t = int(input()) # read a line with a single integer
for j in range(1, t + 1):
    n = int(input())
    s = [int(x) for x in input()]
    count = math.ceil(n/2)
    total = sum(s[0:count])
    answer = total
    for i in range(count, len(s)):
        total = total - s[i - count] + s[i]
        if total > answer:
            answer = total
    print("Case #{}: {}".format(j, answer))
