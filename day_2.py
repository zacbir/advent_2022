#!/usr/bin/env python3


mine = {
    'X': {  # Rock
        'base': 1,
        'them': {
            'A': 3,  # Rock
            'B': 0,  # Paper
            'C': 6   # Scissors
        }
    },
    'Y': {  # Paper
        'base': 2,
        'them': {
            'A': 6,  # Rock
            'B': 3,  # Paper
            'C': 0   # Scissors
        }
    },
    'Z': {  # Scissors
        'base': 3,
        'them': {
            'A': 0,  # Rock
            'B': 6,  # Paper
            'C': 3   # Scissors
        }
    }
}


def score(them: str, me: str) -> int:
    base_score = mine[me]['base']
    choice_score = mine[me]['them'][them]
    
    return base_score + choice_score


if __name__ == "__main__":
    total_score = 0
    
    with open('day_2.txt', 'r') as rps:
        rounds = rps.readlines()
    
    for round in rounds:
        round = round.strip()
        them, me = round.split(' ')
        total_score += score(them, me)
    
    print(f'Total score was: {total_score}')
