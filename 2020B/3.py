def solve(s):
    dx = { 'N': 0, 'S': 0, 'E': 1, 'W': -1 }
    dy = { 'N': -1, 'S': 1, 'E': 0, 'W': 0 }
    result_x = 0
    result_y = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c == 'N' or c == 'E' or c == 'S' or c == 'W':
            result_x += dx[c]
            result_y += dy[c]
            i += 1
        elif c == '(':
            assert 1 == 0
            pass
        elif c == ')':
            return [result_x, result_y, i]
        else: # digit
            repeat_time = int(c)
            substr = s[i + 2:]
            temp_result = solve(s[i + 2:])
            result_x += temp_result[0] * repeat_time
            result_y += temp_result[1] * repeat_time
            i += 2 + temp_result[2] + 1
    return [result_x, result_y, i]


t = int(input()) # read a line with a single integer
limit = 10 ** 9
for i in range(1, t + 1):
    s = input().strip()
    result = solve(s)
    w = (result[0] + limit) % limit + 1
    h = (result[1] + limit) % limit + 1
    print("Case #{}: {} {}".format(i, w, h))
