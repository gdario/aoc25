from load_data import load_data

data = load_data('part1', 'real')
data = [line.strip() for line in data]
data = [[int(_) for _ in line] for line in data]

def listify(s):
    return [int(_) for _ in s]


# This is awfully complicated. There must be a MUCH better way.
def get_joltage(s, size=12):
    digits = []
    for k in range(size-1, 0, -1):
        v = max(s[:-k])
        i = s[:-k].index(v)
        digits.append(v)
        if i == len(s) - k - 1:
            digits.extend(s[i+1:])
            break
        else:
            s = s[i+1:]
    if len(digits) == size - 1:
        digits.append(max(s))
    return int(''.join([str(_) for _ in digits]))
               

def part2():
    return sum([get_joltage(s) for s in data])
