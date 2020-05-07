import math

# first extracting the lone digit, e.g. 124
# then try to add pairs of digit, e.g. 33 => become 12334
# if 124 is a failed case, in order for 12334 to succeed, then 33 must be put in the same side (otherwise the two 3s cancel each other)
# by the same argument, if we are to add 3s again => 1233334, then all the 3s must be put in the same side
# therefore each digit, regardless of its count, must be all put into the same side when added
# here assumes trying until at most 21 counts of each digit is enough, but don't know how to prove

def solve(a):
    digits = [(index, count) for (index, count) in enumerate(a) if count > 0]
    if len(digits) == 1:
        return "YES" if digits[0][1] % 2 == 0 else "NO"
    effective_digits = [(x[0], min(22, x[1]) if x[1] % 2 == 0 else min(21, x[1]) - 1) for x in digits]
    effective_digits = [x for x in effective_digits if x[1] > 0]
    minimum_digits = [(x[0], 1) for x in digits if x[1] % 2 == 1]
    if len(minimum_digits) == 0:
        return "YES"
    last_digit_added = [-1]
    remaining_digits = [effective_digits]
    queue = [minimum_digits]
    walker = 0
    while len(queue) >= walker + 1:
        solve_digits = queue[walker][1:]
        solve_left_total = queue[walker][0][0] * queue[walker][0][1]
        solve_left_count = queue[walker][0][1]
        count_limit = math.ceil(sum([x[1] for x in queue[walker]])/2)
        if solve2(solve_digits, solve_left_total, solve_left_count, 0, 0, count_limit):
            return "YES"
        for x in remaining_digits[walker]:
            if x[0] < last_digit_added[walker]:
                continue
            added = False
            new_digits = []
            for d in queue[walker]:
                cnt = d[1]
                if d[0] == x[0]:
                    added = True
                    cnt += 2
                new_digits.append((d[0], cnt))
            if not added:
                new_digits.append((x[0], 2))
            queue.append(new_digits)
            last_digit_added.append(x[0])
            remaining_digits.append([
                (d[0], d[1] - (2 if x[0] == d[0] else 0))
                for d in remaining_digits[walker]
                if d[1] - (2 if x[0] == d[0] else 0) > 0
            ])
        walker += 1

    return "NO"

def solve2(d, l_t, l_c, r_t, r_c, limit): # same digits go to same side
    if len(d) == 0:
        result = l_t % 11 == r_t % 11 and abs(l_c - r_c) <= 1
        return l_t % 11 == r_t % 11 and abs(l_c - r_c) <= 1
    digit = d[0][0]
    count = d[0][1]
    ok_for_left = l_c + count <= limit
    ok_for_right = r_c + count <= limit
    if ok_for_left and ok_for_right:
        return \
                solve2(d[1:], l_t + digit * count, l_c + count, r_t, r_c, limit) or \
                solve2(d[1:], l_t, l_c, r_t + digit * count, r_c + count, limit)
    if ok_for_left:
        return solve2(d[1:], l_t + digit * count, l_c + count, r_t, r_c, limit)
    if ok_for_right:
        return solve2(d[1:], l_t, l_c, r_t + digit * count, r_c + count, limit)
    return False

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    a = [0] + [int(x) for x in input().split(" ")]
    print("Case #{}: {}".format(i, solve(a)))
