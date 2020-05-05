visited = []

def print_grid(g):
    for row in g:
        print("".join(row))

def print_visited():
    for row in visited:
        print("".join(row))

def solve(n, grid, initial_squares, total_diagonal):
    global visited
    is_even = n % 2 == 0
    visited = [['-' for i in range(n)] for j in range(n)]
    diagonal_flipped = 0

    for square in initial_squares:
        visited[square[0]][square[1]] = 'L'
    square_queue = [(s[0], s[1], 'L') for s in initial_squares]
    walker = 0
    while len(square_queue) > walker:
        x = square_queue[walker][0]
        y = square_queue[walker][1]
        direction = 'R' if square_queue[walker][2] == 'L' else 'L'
        if visited[x][y] == 'C' or direction ==  visited[x][y]:
            walker += 1
            continue

        # flip if necessary
        to_flip = False
        if grid[x][y] == '.': # need to flip
            diagonal_flipped += 1
            to_flip = True

        # visit it and add to queue
        if direction == 'R':
            for i in range(-min(x, y), min(n - x, n - y)):
                if visited[x + i][y + i] == 'L':
                    visited[x + i][y + i] = 'C'
                else:
                    visited[x + i][y + i] = 'R'
                    square_queue.append((x + i, y + i, 'R'))
                if to_flip:
                    grid[x + i][y + i] = '#' if grid[x + i][y + i] == '.' else '.'
        else:
            for i in range(max(-x, -(n - 1 - y)), min(n - 1 - x, y) + 1):
                if visited[x + i][y - i] == 'R':
                    visited[x + i][y - i] = 'C'
                else:
                    visited[x + i][y - i] = 'L'
                    square_queue.append((x + i, y - i, 'L'))
                if to_flip:
                    grid[x + i][y - i] = '#' if grid[x + i][y - i] == '.' else '.'

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
