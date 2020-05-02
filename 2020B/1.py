def solve(h):
    peak = 0
    for i in range(1, len(h) - 1):
        if h[i - 1] < h[i] and h[i] > h[i + 1]:
            peak += 1
    return peak


t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    h = [int(x) for x in input().split(" ")]
    print("Case #{}: {}".format(i, solve(h)))
