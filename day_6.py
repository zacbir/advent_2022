#!/usr/bin/env python3


packet_start_length = 14 #  4 for Part 1


def process_signal(signal: str, packet_length: int) -> int|None:
    for i in range(len(signal) - packet_length):
        candidate = set(signal[i:i+packet_length])
        if len(candidate) == packet_length:
            return i + packet_length
    return None

def main(file_path: str) -> int|None:
    with open(file_path, 'r') as datastream:
        datastream_signal = datastream.readline()
    
    return process_signal(datastream_signal, packet_start_length)


if __name__ == "__main__":
    starting_pos = main('day_6.txt')
    
    if starting_pos is not None:
        print(f'The first position that marks the beginning is {starting_pos}')
    else:
        print(f'The starting position could not be found')
