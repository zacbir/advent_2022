#!/usr/bin/env python3
import re

from day_5 import crates, move_pattern, read_moves


def move_crates(number: int, from_stack: int, to_stack: int):
    intermediate_batch = []
    for i in range(number):
        intermediate_batch.append(crates[from_stack].pop())
    
    crates[to_stack].extend(reversed(intermediate_batch))


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

    print(f'The top of the crates spell "{crate_tops}"')
