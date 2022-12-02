#!/usr/bin/env python3


intent = {
    'X': {  # Lose
        'A': 'Z',  # They play Rock, I should play Scissors
        'B': 'X',  # They play Paper, I should play Rock
        'C': 'Y'   # They play Scissors, I should play Paper
    },
    'Y': {  # Draw
        'A': 'X',  # They play Rock, I should play Rock
        'B': 'Y',  # They play Paper, I should play Paper
        'C': 'Z'   # They play Scissors, I should play Scissors
    },
    'Z': {  # Win
        'A': 'Y',  # They play Rock, I should play Paper
        'B': 'Z',  # They play Paper, I should play Scissors
        'C': 'X'   # They play Scissors, I should play Rock
    }
}

mine = {
    'X': {  # Rock
        'base': 1,
        'A': 3,  # Rock
        'B': 0,  # Paper
        'C': 6   # Scissors
    },
    'Y': {  # Paper
        'base': 2,
        'A': 6,  # Rock
        'B': 3,  # Paper
        'C': 0   # Scissors
    },
    'Z': {  # Scissors
        'base': 3,
        'A': 0,  # Rock
        'B': 6,  # Paper
        'C': 3   # Scissors
    }
}


def score(them: str, me: str) -> int:
    my_play = intent[me][them]

    base_score = mine[my_play]['base']
    choice_score = mine[my_play][them]
    
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
