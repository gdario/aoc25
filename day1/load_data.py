def load_data(part='part1', what='test'):
    filename = part + '.txt'
    if what == 'test':
        filename = 'test_' + filename
    with open(filename, 'r') as fh:
        data = fh.readlines()
    return data
