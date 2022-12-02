

with open('advent_of_code_2022/dayone/calorie_counting_input.txt', 'r') as file:
    input_lines = file.readlines()

elves = [0]

for line in input_lines:
    line = line.strip()
    if line == "":
        elves.append(0)
        continue
    
    elves[-1] += int(line)

elves.sort()

# print(elves)
print(f"Max elf: {elves[-1]}")
print(f"Top three: {elves[-1] + elves[-2] + elves[-3]}")