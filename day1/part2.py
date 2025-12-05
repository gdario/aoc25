# Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:
# 
# The dial starts by pointing at 50.
# The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
# The dial is rotated L30 to point at 52.
# The dial is rotated R48 to point at 0.
# The dial is rotated L5 to point at 95.
# The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
# The dial is rotated L55 to point at 0.
# The dial is rotated L1 to point at 99.
# The dial is rotated L99 to point at 0.
# The dial is rotated R14 to point at 14.
# The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
# In this example, the dial points at 0 three times at the end of a rotation,
# plus three more times during a rotation. So, in this example, the new password
# would be 6.
rotations = []

with open('part1.txt', 'r') as fh:
    for line in fh:
        value = int(line.strip()[1:])
        rotations.append(-1*value if line.startswith('L') else value)


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
                return 1 + abs(rot) // 100
 

def count_zero_crossings(rots, start=50, print_res=False):
    counter = 0
    for rot in rots:
        new_start = (start + rot) % 100
        counter += zero_crossings(start, rot)
        if print_res:
            print(
                f"Start: {start:<5}; Rot: {rot:<7}; " +
                f"End: {(start + rot) % 100:<5}; Counter: {counter:<5}"
            )
        start = new_start
    return counter


def main():
        print(count_zero_crossings(rotations, print_res=True))


main()


if __name__ == '__main__':
    mots = """L68
    L30
    R48
    L5
    R60
    L55
    L1
    L99
    R14
    L82""".splitlines()
    mots = [m.strip() for m in mots]

    mots = [-1*int(m[1:]) if m.startswith('L') else int(m[1:])
            for m in mots]
    # print(count_zero_crossings(mots, print_res=True))
