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

def solve(n, grid, initial_squares, total_diagonal):
    global visited
    global visited_L
    global visited_R
    is_even = n % 2 == 0
    visited = [[0 for i in range(n)] for j in range(n)]
    visited_L = [[0 for i in range(n)] for j in range(n)]
    visited_R = [[0 for i in range(n)] for j in range(n)]
    diagonal_flipped = 0

    # test corner
    for square in initial_squares:
        visited[square[0]][square[1]] = 1
        visited_L[square[0]][square[1]] = 1
    square_queue = [(s[0], s[1], 'L') for s in initial_squares]
    walker = 0
    while len(square_queue) > walker:
        x = square_queue[walker][0]
        y = square_queue[walker][1]
        to_right = square_queue[walker][2] == 'L'
        if (to_right and visited_R[x][y] == 1) or (not to_right and visited_L[x][y] == 1):
            walker += 1
            continue

        # flip if necessary
        to_flip = False
        if grid[x][y] == '.': # need to flip
            diagonal_flipped += 1
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
                square_queue.append((x + i, y + i, 'R'))
        else:
            for i in range(max(-x, -(n - 1 - y)), min(n - 1 - x, y) + 1):
                visited[x + i][y - i] += 1
                visited_L[x + i][y - i] += 1
                if to_flip:
                    grid[x + i][y - i] = '#' if grid[x + i][y - i] == '.' else '.'
                if i == 0:
                    continue
                square_queue.append((x + i, y - i, 'L'))

        walker += 1
    return min(diagonal_flipped, total_diagonal - diagonal_flipped)

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    grid = []
    for j in range(0, n):
        grid.append(list(input()))
    diagonal_count_edge = n * 2 - 1 if n % 2 == 0 else (n - 1) * 2
    diagonal_count_corner = n * 2 - 1 if n % 2 == 0 else n * 2
    ans = solve(n, grid, [(0, 0)], diagonal_count_corner) + solve(n, grid, [(0, 1), (1, 0)], diagonal_count_edge)
    print("Case #{}: {}".format(i, ans))
