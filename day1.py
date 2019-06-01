import decorators
from itertools import accumulate, cycle, tee


@decorators.timer
@decorators.fileio('day1_input')
def part1(data):
    freq = (int(item.strip().strip('+')) for item in data.readlines())
    print(f'part1: {sum(freq)}')

@decorators.timer
@decorators.fileio('day1_input')
def part2(data):
    freq = (int(item.strip().strip('+')) for item in data.readlines())
    freq_set = set()
    for item in accumulate(cycle(freq)):
        if item in freq_set:
            print(f'part2: {item}')
            break
        freq_set.add(item)
    # print(freq_set)

if __name__ == '__main__':
    part1()
    part2()