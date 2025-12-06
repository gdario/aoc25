from load_data import load_data

data = load_data('part1', 'real')
data = [s.strip() for s in data]
data = [-int(s[1:]) if s.startswith('L') else int(s[1:]) for s in data]


def zero_crossings(start, rot):
    rounds, end = divmod(start + rot, 100)
    if rot >= 0:
        return rounds
    else:
        if start == 0:
            return abs(rot) // 100
        else:
            if start + rot > 0:
                return 0
            else:
                return 1 + (abs(rot) - start) // 100

            
def count_zero_crossings(data, start=50, print_res=False):
    counter = 0
    for rot in data:
        new_start = (start + rot) % 100
        counter += zero_crossings(start, rot)
        if print_res:
            print(
                f"Start: {start:<5}; Rot: {rot:<7}; " +
                f"End: {(start + rot) % 100:<5}; Counter: {counter:<5}"
            )
        start = new_start
    return counter


def part2():
    print(count_zero_crossings(data))


part2()
