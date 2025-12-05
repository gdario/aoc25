with open('part1.txt', 'r') as fh:
    lines = fh.read()

ranges, ids = lines.split('\n\n')
ranges, ids = ranges.split('\n'), ids.split('\n')[:-1]
ids = [int(id) for id in ids]
ranges = [range.split('-') for range in ranges]
ranges = [[int(x), int(y)] for x, y in ranges]


fresh_ids = 0
for id in ids:
    for range in ranges:
        if (id >= range[0]) and (id <= range[1]):
            fresh_ids += 1
            break

# Part 1
print(fresh_ids)

# Part 2
def find_overlaps(ranges):
    # breakpoint()
    ranges.sort(key = lambda x: x[0])
    new_ranges = []
    current = ranges[0].copy()
    for range in ranges: 
        if range[0] <= current[1]:
            current[1] = max(range[1], current[1])
        else:
            new_ranges.append(current)
            current = range.copy()
    new_ranges.append(current)
    return new_ranges


def range_lengths(ranges):
    width = 0
    for range in ranges:
        width = width + range[1] - range[0] + 1
    return width


print(range_lengths(find_overlaps(ranges)))
