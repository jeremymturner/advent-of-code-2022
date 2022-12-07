

def read_input(filename, num_chars):
    with open(filename, 'r') as file:
        while True:
            next_char = file.read(1)
            if not next_char:
                return None
            chars.append(next_char)

            if len(chars) >= num_chars:
                if len(chars[-num_chars:]) == len(set(chars[-num_chars:])):
                    return len(chars)

chars = []
print(read_input('advent_of_code_2022/daysix/input.txt', num_chars=4))

chars = []
print(read_input('advent_of_code_2022/daysix/input.txt', num_chars=14))