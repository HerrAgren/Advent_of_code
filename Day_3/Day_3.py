from pathlib import Path

p = Path(__file__).with_name('input.txt')

comp_list_1 = []
comp_list_2 = []
with p.open("r") as f:
    lines:list = f.readlines()
    for rucksack in lines:
        rucksack = rucksack.replace('\n', '')
        comp_1, comp_2 = rucksack[0:len(rucksack)//2], rucksack[len(rucksack)//2:len(rucksack)]
        comp_list_1.append(comp_1)
        comp_list_2.append(comp_2)



alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mixed_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

scoring_alpabet = []
for i in range(1,53):
    char_and_score = (mixed_alphabet[i-1], i)
    scoring_alpabet.append(char_and_score)


correlated_chars = []
for comp_1, comp_2 in zip(comp_list_1, comp_list_2):
    for char in comp_1:
        if comp_2.find(char) != -1:
            correlated_chars.append(comp_2[comp_2.find(char)])

score = 0

for tup in scoring_alpabet:
    if char == tup[0]:
        score += tup[1]

print(score)