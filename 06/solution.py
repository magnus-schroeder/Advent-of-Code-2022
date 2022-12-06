with open('input.txt') as input_file:
    lines = [line.rstrip() for line in input_file]


def get_marker(size):
    for line in lines:
        for i in range(len(line)):
            if len(set(line[i:i + size])) == size:
                return i + size


print(get_marker(4))
print(get_marker(14))
