
lst = []
with open("input.txt", "r") as f:
    line = f.readlines()
    current_elf = []
    for number in line:
        if number == '\n':
            calories_of_elf = sum(current_elf)
            lst.append(calories_of_elf)
            current_elf = []
        else:
            number = int(number)
            current_elf.append(number)


top_three = []
for i in range(0,3):
    max_now = max(lst)
    lst.remove(max_now)
    top_three.append(max_now)

print(len(top_three))
print(sum(top_three))
    