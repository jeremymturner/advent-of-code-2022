import json

def read_initial_stack_line(line):
    """ Read the initial state of the stacks """
    stack_cols = []
    if line[1] == '1':
        return None
    for index,box in enumerate(line):
        if index % 4 == 1:
            if box != ' ':
                stack_cols.append(box)
            else:
                stack_cols.append(None)
    return stack_cols

def read_instructions_line(line):
    """ Read the list of instructions """
    line = line.strip()
    items = line.split(' ')
    return { "count": int(items[1]), "source": int(items[3])-1, "dest": int(items[5])-1}

def read_input(lines):
    """ Read the input """
    initial_stacks = []
    initial = True
    instructions = []
    for line in lines:
        if line == '\n':
            initial = False
        elif initial:
            initial_line = read_initial_stack_line(line)
            if initial_line:
                initial_stacks.append(initial_line)
        else:
            instructions.append(read_instructions_line(line))


    return { "initial_stacks": initial_stacks,
             "instructions": instructions
    }

def process_instructions(data):
    # deal with the stacks first
    initial_stacks = data.get("initial_stacks")
    initial_stacks.reverse()
    stacks = []

    # rotate the array of arrays into columnar order, bottom first
    for row in initial_stacks:
        for index, box in enumerate(row):
            print(index, row, box)
            if len(stacks) == index:
                stacks.append([])
            if box:
                stacks[index].append(box)

    # apply instructions
    instructions = data.get("instructions")

    # part one stacks
    # for instruction in instructions:
    #     for i in range(instruction.get("count")):
    #         stacks[instruction.get("dest")].append(stacks[instruction.get("source")].pop())
    
    # part two stacks
    for instruction in instructions:
        temp = []
        for i in range(instruction.get("count")):
            temp.insert(0, stacks[instruction.get("source")].pop())
        stacks[instruction.get("dest")].extend(temp)

    top = ""
    for col in stacks:
        top += col[-1]


    return top

with open('advent_of_code_2022/dayfive/input.txt', 'r') as file:
    lines = file.readlines()
before_data = read_input(lines)
after_data = process_instructions(before_data)
print(json.dumps(before_data, indent=2))
print(json.dumps(after_data, indent=2))
