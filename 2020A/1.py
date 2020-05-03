t = int(input())
for i in range(1, t + 1):
    n, b = [int(x) for x in input().split(" ")]
    a = [int(x) for x in input().split(" ")]
    a.sort()
    count = 0
    total = 0
    for a_i in a:
        if total + a_i > b:
            break
        count += 1
        total += a_i
    print("Case #{}: {}".format(i, count))
