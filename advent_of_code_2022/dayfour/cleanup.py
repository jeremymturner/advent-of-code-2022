
with open('advent_of_code_2022/dayfour/input.txt', 'r') as file:
    input_lines = file.readlines()

sum_overlap = 0
sum_partial = 0
for line in input_lines:
    line = line.strip()
    elf1, elf2 = line.split(',')
    elf1a, elf1b = elf1.split('-')
    elf2a, elf2b = elf2.split('-')
    elf1a = int(elf1a)
    elf1b = int(elf1b)
    elf2a = int(elf2a)
    elf2b = int(elf2b)

    if elf1a >= elf2a and elf1b <= elf2b:
        print(1, '-', elf1a, elf1b, elf2a, elf2b, line)
        sum_overlap += 1

    elif elf2a >= elf1a and elf2b <= elf1b:
        print(2, '-', elf1a, elf1b, elf2a, elf2b, line)
        sum_overlap += 1

    elif elf1b >= elf2a and elf1b <= elf2b:
        print(3, '-', elf1a, elf1b, elf2a, elf2b, line)
        sum_partial += 1

    elif elf2b >= elf1a and elf2a <= elf1a:
        print(4, '-', elf1a, elf1b, elf2a, elf2b, line)
        sum_partial += 1


print(f"part one {sum_overlap}")
print(f"part two {sum_partial + sum_overlap}")
