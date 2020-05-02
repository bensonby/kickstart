def solve(n, d, x):
    peak = 0
    for i in range(n - 1, -1, -1):
        d = d - d % x[i]
    return d


t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    (n, d) = [int(x) for x in input().split(" ")]
    x = [int(x) for x in input().split(" ")]
    print("Case #{}: {}".format(i, solve(n, d, x)))
