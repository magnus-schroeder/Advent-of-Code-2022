with open('input.txt') as input_file:
    lines = [line.rstrip() for line in input_file]


def get_marker(size):
    for line in lines:
        for i in range(len(line)):
            chars = set()
            for j in range(size):
                chars.add(line[i + j])
            if len(chars) == size:
                return i + size


print(get_marker(4))
print(get_marker(14))
