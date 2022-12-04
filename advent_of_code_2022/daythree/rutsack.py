import string

with open('advent_of_code_2022/daythree/input.txt', 'r') as file:
    input_lines = file.readlines()

# priority list (0-indexed, so need to add one after getting the index)
priority = list(string.ascii_lowercase) + list(string.ascii_uppercase)

extra_sum = 0
elf_group = 0
elf_group_items = []
badge_sum = 0

for rutsack in input_lines:
    rutsack = rutsack.strip()

    elf_group_items.append(rutsack)

    # split the string up
    length = int(len(rutsack) / 2)
    comp1 = rutsack[0:length]
    comp2 = rutsack[length:]
    common = list(set(comp1) & set(comp2))[0]

    print(elf_group, common, rutsack, length, comp1, comp2, priority.index(common)+1)
    extra_sum += priority.index(common)+1
    elf_group += 1
    # calculate and reset
    if elf_group == 3:
        badge = list(set(elf_group_items[0]) & set(elf_group_items[1]) & set(elf_group_items[2]))[0]
        badge_priority = priority.index(badge)+1
        badge_sum += badge_priority
        elf_group = 0
        elf_group_items = []

print(extra_sum)
print(badge_sum)
