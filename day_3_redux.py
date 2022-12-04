#!/usr/bin/env python3
import string
from typing import List


priorities = dict(zip(list(string.ascii_letters), range(1, 53)))


def process_batch(packs: List[str]) -> str:
    pack_1 = set(packs[0].strip())
    pack_2 = set(packs[1].strip())
    pack_3 = set(packs[2].strip())
    
    common = pack_1 & pack_2 & pack_3
    
    return priorities[common.pop()]


def main(file_path: str) -> int:
    total = 0
    batch_size = 3
    
    with open(file_path, 'r') as pack_file:
        pack_list = pack_file.readlines()
    
    for i in range(0, len(pack_list), batch_size):
        total += process_batch(pack_list[i:i+batch_size])
    
    return total


if __name__ == "__main__":
    total = main('day_3.txt')
    
    print(f'The total of all groups\' priorities is {total}')
