# Start at 50
# If L multiply by -1
# (current + rotation) % 100 -> new position

motions = []


with open('part1.txt', 'r') as fh:
    for line in fh:
        value = int(line[1:])
        motions.append(-1*value if line.startswith('L') else value)


def count_zeros(motions, start=50):
    counter = 0
    for motion in motions:
        start = (start + motion) % 100
        if start == 0:
            counter += 1
    return counter


print(count_zeros(motions))


def bubu(start, shift):
    rounds = abs(shift) // 100
    if start >=0 and shi


If __name__ == '__main__':
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

mots = [-1*int(m[1:]) if m.startswith('L') else int(m[1:])
           for m in mots]
print(sign(1) == sign(-1))
print(mots)
print(count_zero_crossing(mots))
