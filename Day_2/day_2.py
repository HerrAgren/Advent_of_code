from pathlib import Path

p = Path(__file__).with_name('input.txt')

def convert_char_to_hand(char):
    if char is 'A' or char is 'X':
        return 'Rock'
    if char is 'B' or char is 'Y':
        return 'Paper'
    if char is 'C' or char is 'Z':
        return 'Scissor'


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

        
        

print(opponent_list)