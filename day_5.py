#!/usr/bin/env python3
import re
from typing import List


# the initial stack representation will be hard-coded
crates = [
    [],  # 0, this makes it easier to deal with the moves which are 1-based
    list('ZJNWPS'),
    list('GST'),
    list('VQRLH'),
    list('VSTD'),
    list('QZTDBMJ'),
    list('MWTJDCZL'),
    list('LPMWGTJ'),
    list('NGMTBFQH'),
    list('RDGCPBQW')
]

move_pattern = re.compile(r'^move (?P<number>\d+) from (?P<from_stack>\d+) to (?P<to_stack>\d+)$')


def move_crates(number: int, from_stack: int, to_stack: int):
    for x in range(number):
        crate = crates[from_stack].pop()
        crates[to_stack].append(crate)


def read_moves(file_path: str) -> List[str]:
    # filter the file when reading to just include lines that begin with 'move'
    with open(file_path, 'r') as crate_moves_file:
        crate_moves = [line for line in crate_moves_file.readlines()
                       if line.startswith('move')]

    return crate_moves


def main(file_path: str) -> str:
    crate_moves = read_moves(file_path)
    
    for move in crate_moves:
        match = move_pattern.match(move)
        number = int(match.group('number'))
        from_stack = int(match.group('from_stack'))
        to_stack = int(match.group('to_stack'))
        
        move_crates(number, from_stack, to_stack)
        
    return ''.join([crate[-1] for crate in crates[1:]])


if __name__ == "__main__":
    crate_tops = main('day_5.txt')
    
    print(f'The top crates are "{crate_tops}"')