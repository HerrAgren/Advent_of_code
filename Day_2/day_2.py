from pathlib import Path

p = Path(__file__).with_name('input.txt')

def convert_char_to_hand(char):
    if char == 'A' or char == 'X':
        return 'Rock'
    elif char == 'B' or char == 'Y':
        return 'Paper'
    elif char == 'C' or char == 'Z':
        return 'Scissor'

def score_my_hand(opponent_hand, my_hand):
    score_to_return = 0
    if my_hand =='Rock':
        score_to_return += 1
    elif my_hand =='Paper':
        score_to_return += 2
    elif my_hand == 'Scissor':
        score_to_return += 3

    if my_hand == opponent_hand:
        score_to_return += 3
        return score_to_return

    if my_hand == 'Rock':
        if opponent_hand == 'Scissor':
            score_to_return += 6
            return score_to_return
        elif opponent_hand == 'Paper':
            return score_to_return

    elif my_hand == 'Paper':
        if opponent_hand == 'Scissor':
            return score_to_return
        elif opponent_hand == 'Rock':
            score_to_return += 6
            return score_to_return

    elif my_hand == 'Scissor':
        if opponent_hand == 'Rock':
            return score_to_return
        elif opponent_hand == 'Paper':
            score_to_return += 6
            return score_to_return





opponent_list = []
my_list = []
with p.open("r") as f:
    line = f.readlines()
    current_elf = []
    for number in line:
        opponents_hand, my_hand = number.split(' ')
        opponents_hand = opponents_hand[0]
        my_hand = my_hand[0]
        opponent_list.append(convert_char_to_hand(opponents_hand))
        my_list.append(convert_char_to_hand(my_hand))

score_sum = 0    
for x,y in zip(opponent_list,my_list):
    score = score_my_hand(x,y)
    score_sum += score
print(score_sum)
