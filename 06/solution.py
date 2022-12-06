line = open('input.txt').read()


def get_marker(size):
    for i in range(len(line)):
        if len(set(line[i:i + size])) == size:
            return i + size
    return None


print(get_marker(4))
print(get_marker(14))
