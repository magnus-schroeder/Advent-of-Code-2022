with open('input.txt') as input_file:
    lines = [line.rstrip() for line in input_file]

filesystem = {'/': dict()}
directories = list()

path = list()
for i in range(len(lines)):
    line = lines[i]

    if line == '$ cd ..':
        path.pop()
    elif line.startswith('$ cd'):
        path.append(line[5:])
    elif line == '$ ls':
        next_line_index = i + 1
        while next_line_index < len(lines) and not lines[next_line_index].startswith('$'):
            next_line = lines[next_line_index]
            current_directory = filesystem

            for step in path:
                current_directory = current_directory[step]
            if next_line.startswith('dir'):
                name = next_line[4:]
                current_directory[name] = dict()
                directories.append(path[:] + [name])
            else:
                size, name = next_line.split(' ')
                current_directory[name] = int(size)
            next_line_index += 1


def get_size(path_to_directory):
    directory_size = 0
    current_directory = filesystem
    for step in path_to_directory:
        current_directory = current_directory[step]
    for key, val in current_directory.items():
        if type(val) is dict:
            directory_size += get_size(path_to_directory + [key])
        else:
            directory_size += val
    return directory_size


directories = list(map(lambda directory: get_size(directory), directories))
total_size = get_size(['/'])

print(sum(list(filter(lambda directory: directory <= 100000, directories))))
print(sorted(list(filter(lambda directory: 40000000 - total_size + directory >= 0, directories)))[0])
