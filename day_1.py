#!/usr/bin/env python3
import uuid


class Elf:
    def __init__(self):
        self.name = uuid.uuid4()
        self.slots = []
    
    def stash(self, caloric_thing: int):
        self.slots.append(caloric_thing)
        
    def total_calories(self) -> int:
        return sum(self.slots)


class Expedition:
    def __init__(self):
        self._elves = []
    
    def add_elf(self, elf: Elf):
        self._elves.append(elf)
    
    def sorted_elves(self) -> list[Elf]:
        return list(reversed(sorted(self._elves, key=lambda e: e.total_calories())))
    
    def max_calories(self) -> int:
        return self.top_carriers(1)[0]
    
    def top_carriers(self, number: int) -> list[int]:
        return [x.total_calories() for x in self.sorted_elves()[:number]]


def main(file_path: str) -> Expedition:
    expedition = Expedition()
    current_elf = Elf()

    with open(file_path, 'r', newline='\n') as infile:
        lines = infile.readlines()
    
    for line in lines:
        caloric_thing = line.strip()
        if caloric_thing:
            # add the caloric_thing to the current_elf
            current_elf.stash(int(caloric_thing))
        else:
            # add current_elf to our expedition and get the next one
            expedition.add_elf(current_elf)
            print(f'Elf {current_elf.name} carries {current_elf.total_calories()} calories.')
            current_elf = Elf()
            next
        
    return expedition

 
if __name__ == "__main__":
    expedition = main('day_1.txt')

    print(f'Highest calories carried by an elf is {expedition.max_calories()}')

    print(f'The three highest carriers have: {sum(expedition.top_carriers(3))}')