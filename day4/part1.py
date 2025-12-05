with open('part1.txt', 'r') as fh:
    lines = fh.readlines()

grid = [[int(ch == '@') for ch in line.strip()] for line in lines]
test_grid = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".split('\n')

test_grid = [[int(ch == '@') for ch in line.strip()] for line in test_grid]


def pad_grid(g):
    nrows = len(g)
    ncols = len(g[0])
    padded = [[0 for _ in range(ncols + 2)] for _ in range(nrows + 2)]
    for i in range(nrows):
        for j in range(ncols):
            padded[i+1][j+1] = g[i][j]
    return padded


def count_neigbours(g):
    nrows, ncols = len(g), len(g[0])
    p = pad_grid(g)
    counts = [[0 for _ in range(ncols)] for _ in range(nrows)]
    for i in range(1, nrows+2):
        for j in range(1, ncols+2):
            if p[i][j] == 1:
                counts[i-1][j-1] = p[i-1][j-1] + p[i-1][j] + p[i-1][j+1] + \
                        p[i][j-1] + p[i][j+1] + \
                        p[i+1][j-1] + p[i+1][j] + p[i+1][j+1]
    return counts


def part1(grid):
    result = 0
    counts = count_neigbours(grid)
    for i in range(len(counts)):
        for j in range(len(counts[0])):
            if grid[i][j] == 1 and counts[i][j] < 4:
                result += 1
    return result


def part2(grid):
    removed = 100
    tot_removed = 0
    while removed > 0:
        counts = count_neigbours(grid)
        removed = 0
        for i in range(len(counts)):
            for j in range(len(counts[0])):
                if grid[i][j] == 1 and counts[i][j] < 4:
                    grid[i][j] = 0
                    removed += 1
        # print(f'removed: {removed}')
        tot_removed += removed
    return tot_removed


if __name__ == '__main__':
    print(part1(grid))
    print(part2(grid))
