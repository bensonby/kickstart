def solve(n, p, s):
    s.sort()
    target_s = s[p - 1]
    next_index = p - 1
    while next_index < n and s[next_index] == target_s:
        next_index += 1
    ans = sum([target_s - x for x in s[next_index - p:next_index]])
    if next_index >= n:
        return ans
    current = ans
    while next_index < n:
        next_target_s = s[next_index]
        # break
        diff = next_target_s - target_s
        count = 0
        while next_index < n and s[next_index] == next_target_s:
            count += 1
            current -= (target_s - s[next_index - p])
            next_index += 1
        current += (p - count) * diff
        if current < ans:
            ans = current
        target_s = next_target_s
    return ans


t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n, p = [int(x) for x in input().split(" ")]
    s = [int(x) for x in input().split(" ")]
    print("Case #{}: {}".format(i, solve(n, p, s)))
