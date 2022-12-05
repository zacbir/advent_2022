#!/usr/bin/env python3
from typing import Tuple

def main(file_path: str) -> Tuple[int, int]:
    num_overlapping = num_fully_contained = 0
    
    with open(file_path, 'r') as pair_list_file:
        pair_list = pair_list_file.readlines()
    
    for pair in pair_list:
        elf_1_range, elf_2_range = pair.split(',')
        elf_1_lower, elf_1_upper = elf_1_range.split('-')
        elf_2_lower, elf_2_upper = elf_2_range.split('-')

        elf_1 = set(range(int(elf_1_lower), int(elf_1_upper) + 1))
        elf_2 = set(range(int(elf_2_lower), int(elf_2_upper) + 1))
        
        elf_intersection = elf_1.intersection(elf_2)
        if elf_intersection:  # There's overlap at all
            num_overlapping += 1
            if elf_intersection in [elf_1, elf_2]:
                num_fully_contained += 1
    
    return num_overlapping, num_fully_contained

if __name__ == "__main__":
    num_overlapping, num_fully_contained = main("day_4.txt")

    print(f'There were {num_overlapping} overlaps, and {num_fully_contained} where one elf fully contains the other.')