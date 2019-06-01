import decorators
from itertools import accumulate, cycle


@decorators.timer
@decorators.fileio('day1_input')
def part1(data):
    freq = (int(item.strip().strip('+')) for item in data.readlines())
    return sum(freq)

@decorators.timer
@decorators.fileio('day1_input')
def part2(data):
    freq = (int(item.strip().strip('+')) for item in data.readlines())
    freq_set = set([0])
    for item in accumulate(cycle(freq)):
        if item in freq_set:
            return item
        freq_set.add(item)
    # print(freq_set)

if __name__ == '__main__':
    print(f'part1: {part1()}')
    print(f'part2: {part2()}')