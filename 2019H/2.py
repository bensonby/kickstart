visited = []
visited_L = []
visited_R = []

def print_grid(g):
    for row in g:
        print("".join(row))

def print_visited():
    for row in visited_L:
        print("".join([str(v) for v in row]))
    for row in visited_R:
        print("".join([str(v) for v in row]))

def solve1(n, grid):
    global visited
    global visited_L
    global visited_R
    is_even = n % 2 == 0
    visited = [[0 for i in range(n)] for j in range(n)]
    visited_L = [[0 for i in range(n)] for j in range(n)]
    visited_R = [[0 for i in range(n)] for j in range(n)]
    diagonal_count_corner = n * 2 - 1 if is_even else n * 2
    diagonal_corner_flipped = 0

    # test corner
    visited[0][0] = 1
    visited_L[0][0] = 1
    square_queue = [(0, 0, 'L')]
    walker = 0
    while len(square_queue) > walker:
        x = square_queue[walker][0]
        y = square_queue[walker][1]
        to_right = square_queue[walker][2] == 'L'
        # if visited[x][y] == 2:
            # print(x, y)
            # assert grid[x][y] == '#'
        if (to_right and visited_R[x][y] == 1) or (not to_right and visited_L[x][y] == 1):
            walker += 1
            continue

        # flip if necessary
        to_flip = False
        if grid[x][y] == '.': # need to flip
            diagonal_corner_flipped += 1
            to_flip = True

        # visit it and add to queue
        if to_right:
            if x == 1 and y == 9:
                'hello to_right'
            assert visited_R[x][y] == 0
            for i in range(-min(x, y), min(n - x, n - y)):
                visited[x + i][y + i] += 1
                visited_R[x + i][y + i] += 1
                if to_flip:
                    grid[x + i][y + i] = '#' if grid[x + i][y + i] == '.' else '.'
                if i == 0:
                    continue
                assert x + i >= 0
                assert x + i < n
                assert y + i >= 0
                assert y + i < n
                square_queue.append((x + i, y + i, 'R'))
        else:
            if x == 1 and y == 9:
                'hello to_left'
            for i in range(max(-x, -(n - 1 - y)), min(n - 1 - x, y) + 1):
                visited[x + i][y - i] += 1
                visited_L[x + i][y - i] += 1
                if to_flip:
                    grid[x + i][y - i] = '#' if grid[x + i][y - i] == '.' else '.'
                if i == 0:
                    continue
                assert x + i >= 0
                assert x + i < n
                assert y - i >= 0
                assert y - i < n
                square_queue.append((x + i, y - i, 'L'))

        walker += 1
    # print('solve1: flipped={}, total={}'.format(diagonal_corner_flipped, diagonal_count_corner))
    return min(diagonal_corner_flipped, diagonal_count_corner - diagonal_corner_flipped)

def solve2(n, grid):
    global visited
    global visited_L
    global visited_R
    is_even = n % 2 == 0
    visited = [[0 for i in range(n)] for j in range(n)]
    visited_L = [[0 for i in range(n)] for j in range(n)]
    visited_R = [[0 for i in range(n)] for j in range(n)]
    diagonal_count_edge = n * 2 - 1 if is_even else (n - 1) * 2
    diagonal_edge_flipped = 0

    # test corner
    visited[0][1] = 1
    visited[1][0] = 1
    visited_L[0][1] = 1
    visited_L[1][0] = 1
    square_queue = [(0, 1, 'L'), (1, 0, 'L')]
    walker = 0
    while len(square_queue) > walker:
        x = square_queue[walker][0]
        y = square_queue[walker][1]
        to_right = square_queue[walker][2] == 'L'
        # if visited[x][y] == 2:
            # print(x, y)
            # assert grid[x][y] == '#'
        if (to_right and visited_R[x][y] == 1) or (not to_right and visited_L[x][y] == 1):
            walker += 1
            continue

        # flip if necessary
        to_flip = False
        if grid[x][y] == '.': # need to flip
            diagonal_edge_flipped += 1
            to_flip = True

        # visit it and add to queue
        if to_right:
            for i in range(-min(x, y), min(n - x, n - y)):
                visited[x + i][y + i] += 1
                visited_R[x + i][y + i] += 1
                if to_flip:
                    grid[x + i][y + i] = '#' if grid[x + i][y + i] == '.' else '.'
                if i == 0:
                    continue
                assert x + i >= 0
                assert x + i < n
                assert y + i >= 0
                assert y + i < n
                square_queue.append((x + i, y + i, 'R'))
        else:
            for i in range(max(-x, -(n - 1 - y)), min(n - 1 - x, y) + 1):
                visited[x + i][y - i] += 1
                visited_L[x + i][y - i] += 1
                if to_flip:
                    grid[x + i][y - i] = '#' if grid[x + i][y - i] == '.' else '.'
                if i == 0:
                    continue
                assert x + i >= 0
                assert x + i < n
                assert y - i >= 0
                assert y - i < n
                square_queue.append((x + i, y - i, 'L'))

        # print_grid(grid)
        # print('--------')
        walker += 1
    # print('flipped={}, total={}'.format(diagonal_edge_flipped, diagonal_count_edge))
    return min(diagonal_edge_flipped, diagonal_count_edge - diagonal_edge_flipped)

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    grid = []
    for j in range(0, n):
        grid.append(list(input()))
    print("Case #{}: {}".format(i, solve1(n, grid) + solve2(n, grid)))
