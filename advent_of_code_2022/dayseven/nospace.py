class directory():
    def __init__(self, name, parent=None):
        self.name = name
        self.files = {}
        self.dirs = {}
        self.size = 0
        self.parent = parent

    def add_file(self, name, size):
        self.files[name] = size
        self.size += size

    def add_dir(self, name):
        self.dirs[name] = directory(name=name, parent=self)
    
    def get_size(self):
        total_size = self.size
        for name, dir in self.dirs.items():
            total_size += dir.get_size()
        return total_size
    
    def get_size_10k(self):
        size = 0
        if self.get_size() <= 100000:
            # print(self.name, self.get_size())
            size += self.get_size()
        for name, dir in self.dirs.items():
            size += dir.get_size_10k()
        return size


    def __str__(self):
        return str(self.files) + str(self.dirs)

    def directory_list(self):
        total_used = 42677139
        total_space = 70000000
        # print(f"{self.name} {total_space} - {total_used}")
        unused_space = total_space - total_used
        smallest_dir_size = 30000000 - unused_space
        if self.get_size() >= smallest_dir_size:
            print(self.name, self.get_size())
        for name, dir in self.dirs.items():
            dir.directory_list()



MY_FILESYSTEM = directory(name="/")
CUR_DIRECTORY = MY_FILESYSTEM

def parse_line(line):
    global CUR_DIRECTORY, MY_FILESYSTEM

    line = line.strip()
    # print(line)

    if line[0:6] == "$ cd /":
        CUR_DIRECTORY = MY_FILESYSTEM

    elif line[0:7] == "$ cd ..":
        # parts = line.split(" ")
        # CUR_DIRECTORY.pop()
        CUR_DIRECTORY = CUR_DIRECTORY.parent

    elif line[0:5] == "$ cd ":
        parts = line.split(" ")
        name = " ".join(parts[2:])
        CUR_DIRECTORY = CUR_DIRECTORY.dirs[name]
        # CUR_DIRECTORY.append(" ".join(parts[2:]))

    elif line[0:4] == "$ ls":
        # print("ls")
        # nothing to do
        pass

    elif line[0:3] == "dir":
        # new_dir = CUR_DIRECTORY + [" ".join(line.split(" ")[2:])]
        new_dir = " ".join(line.split(" ")[1:])
        CUR_DIRECTORY.add_dir(new_dir)
        # print("got a dir")
    
    elif int(line[0]):
        # print("got a file")
        new_file = " ".join(line.split(" ")[1:])
        file_size = int(line.split(" ")[0])
        CUR_DIRECTORY.add_file(new_file, file_size)
    
    # print(CUR_DIRECTORY)

with open("advent_of_code_2022/dayseven/input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    parse_line(line)

# print()
# print(MY_FILESYSTEM)
# print()
# print(MY_FILESYSTEM.get_size())
# print()
# print(MY_FILESYSTEM.dirs["a"].dirs["e"].get_size())
# print()
# print(MY_FILESYSTEM.dirs["d"].get_size())
# print()
print(f"Part One: {MY_FILESYSTEM.get_size_10k()}")
print()

print(MY_FILESYSTEM.get_size())

MY_FILESYSTEM.directory_list()