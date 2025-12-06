import math
from load_data import load_data

data = load_data('part1', 'real')

operators = data[-1].strip().split()
data = [[int(x) for x in line.strip().split()] for line in data[:-1]]

# Transpose
data = zip(*data)

total = 0
for i, x in enumerate(data):
    total += sum(x) if operators[i] == '+' else math.prod(x)

print(total)
