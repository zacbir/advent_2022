#!/usr/bin/env python3
import string


priorities = dict(zip(list(string.ascii_letters), range(1, 53)))


def process_line(line: str) -> int:
    # take the length of the line, divide it by two
    # take each half and turn them each into a set
    # find the intersection of the sets
    # return its value from the priorities dict
    pack_1 = set(line[:len(line)//2])
    pack_2 = set(line[len(line)//2:])

    common = pack_1.intersection(pack_2)
    
    return priorities[common.pop()]


def main(file_path: str) -> int:
    total = 0
    
    with open(file_path, 'r') as pack_file:
        packs = pack_file.readlines()
        
    for pack in packs:
        total += process_line(pack)
    
    return total

if __name__ == "__main__":
    total = main('day_3.txt')

    print(f'Total priorities of all packs is {total}')