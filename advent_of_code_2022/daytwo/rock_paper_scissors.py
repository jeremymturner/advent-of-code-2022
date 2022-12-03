

with open('advent_of_code_2022/daytwo/rps_sample_input.txt', 'r') as file:
    input_lines = file.readlines()

part_one_points = {
    'BX': 1, # lose
    'CY': 2,
    'AZ': 3,

    'AX': 4, # draw
    'BY': 5,
    'CZ': 6,

    'CX': 7, # win
    'AY': 8,
    'BZ': 9
}

part_two_points = {
    'BX': 1, # lose
    'CX': 2,
    'AX': 3,

    'AY': 4, # draw
    'BY': 5,
    'CY': 6,

    'CZ': 7, # win
    'AZ': 8,
    'BZ': 9
}


part_one_sum = 0
part_two_sum = 0
for line in input_lines:
    game = ''.join(line.strip().split(' '))
    part_one_sum += part_one_points.get(game,0)
    part_two_sum += part_two_points.get(game,0)

print(f"part one sum: {part_one_sum}")
print(f"part two sum: {part_two_sum}")
