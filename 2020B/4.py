import math

def prob_to_end(base, n, i):
    result = base[1]
    tmp_base = base[0]
    for r in range(i + 1, n + 1):
        # print(base, n, r)
        tmp_base = tmp_base - math.log(r, math.e) + math.log(n + 1 - r, math.e)
        result += math.exp(tmp_base)
    # sum(nCr for r from i to n) / 2^n
    return result

def prob(n, i):
    result = 0
    # nCi / 2^n
    i = max(i, n - i)
    divide_list = list(range(n - i, 1, -1)) + [2] * n
    for x in range(n, i, -1):
        result += math.log(x, math.e)
    for x in divide_list:
        result -= math.log(x, math.e)
    return [result, math.exp(result)]

def solve(w, h, l, u, r, d):
    bad_prob = 0
    base_prob = 0
    for row in range(u, d + 1):
        prev_bad = bad_prob
        if l == 1:
            continue
        if row == u:
            base_prob = prob(row + l - 3, row - 1)
        else:
            base_prob[0] = base_prob[0] + math.log(row + l - 3, math.e) - math.log(row - 1, math.e) - math.log(2, math.e)
            base_prob[1] = math.exp(base_prob[0])
        if row == h:
            bad_prob += prob_to_end(base_prob, row + l -3, row - 1)
        else:
            bad_prob += base_prob[1] * 0.5
        # print(row + l - 3, row - 1, bad_prob - prev_bad)
    for col in range(l, r + 1):
        prev_bad = bad_prob
        if u == 1:
            continue
        if col == l:
            base_prob = prob(col + u - 3, col - 1)
            # print(base_prob)
        else:
            base_prob[0] = base_prob[0] + math.log(col + u - 3, math.e) - math.log(col - 1, math.e) - math.log(2, math.e)
            base_prob[1] = math.exp(base_prob[0])
            # print(base_prob)
        if col == w:
            bad_prob += prob_to_end(base_prob, col + u - 3, col - 1)
        else:
            bad_prob += base_prob[1] * 0.5
        # print(col + u - 3, col - 1, bad_prob - prev_bad, base_prob)
    return 1 - bad_prob


t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    w, h, l, u, r, d = [int(x) for x in input().split(" ")]
    print("Case #{}: {}".format(i, solve(w, h, l, u, r, d)))
