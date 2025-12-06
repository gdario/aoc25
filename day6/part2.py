from math import prod
from load_data import load_data

data = load_data('part1', 'real')
ncols = len(data[0])
nrows = len(data)

tmp = list(zip(*data))
tmp = list(reversed(tmp))[1:]
tmp = [''.join(t) for t in tmp]
tmp = [s.strip() for s in tmp if s.strip() != '']

grand_total = 0
digits = []
for s in tmp:
    if s[-1] in '+*':
        operator = s[-1]
        x = int(s[:-1].strip())
        digits.append(x)
        grand_total += sum(digits) if operator == '+' else prod(digits)
        digits = []
    else:
        digits.append(int(s.strip()))

print(grand_total)
