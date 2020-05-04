from queue import PriorityQueue

def solve(a):
    q = PriorityQueue()
    h = 1
    paper_count = 0
    # h = 4
    # 4, 4, 4, 4, 4, 5
    # 5, 5, 5, 6
    # 4, 5, 5, 5, 6
    # 4, 6, 6, 7
    for x in a:
        if x <= h:
            print(' {}'.format(h), end='')
            continue
        q.put((x, x))
        paper_count += 1
        # print('--x={}, count={}, h={}'.format(x, paper_count, h))
        if paper_count >= h + 1:
            while paper_count > 0 and q.queue[0][0] == h + 1:
                _ = q.get()
                paper_count -= 1
            h += 1
        print(' {}'.format(h), end='')


t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    print("Case #{}:".format(i), end='')
    solve(a)
    print("")
