with open('part1.txt', 'r') as fh:
    data = fh.readlines()

test_data = """987654321111111
811111111111119
234234234234278
818181911112111""".split('\n')

def process_data(data):
    return [[int(x) for x in row.strip()] for row in data]


data, test_data = process_data(data), process_data(test_data)


def get_joltage(d):
    maxv = max(d)
    idx = d.index(maxv)
    if idx < len(d) - 1:
        other = max(d[idx+1:])
        return int(str(maxv) + str(other))
    else:
        other = max(d[:-1])
        return int(str(other) + str(maxv))

# 2342_34234234278 -> 4
# 234 23_4234234278 -> 3
# 23423 4_234234278 -> 

def gen_joltage(d, size=12):
    k = size
    res = []
    while True:
        k -= 1
        v = max(d[:-k])
        i = d.index(v)
        res.append(v)
        d = d[i+1:]
        if len(res) == size:
            return res
        elif i+1 == len(d) - k:
            return res + d[-k]


def part1(d):
    res = [get_joltage(bank) for bank in d]
    # print(res)
    return sum(res)


def part2(d):
    tmp = [gen_joltage(_) for _ in d]
    tmp = [int(''.join([str(_) for _ in line])) for line in d]
    return sum(tmp)

if __name__ == '__main__':
    print([gen_joltage(d) for d in test_data])

