with open('input.txt') as input_file:
    lines = [line.rstrip() for line in input_file]


def get_message(stacks):
    message = ''
    for stack in stacks:
        message += stack.pop()
    return message


stack_end = lines.index(next(filter(lambda line: line != '' and line[1] == '1', lines), None))
first_stacks = [list() for i in range(int(lines[stack_end][-1]))]

for i in range(stack_end):
    for j in range(len(first_stacks)):
        element = lines[i][1 + 4 * j]
        if element != ' ':
            first_stacks[j].append(element)

first_stacks = [list(reversed(stack)) for stack in first_stacks]
second_stacks = [list(stack) for stack in first_stacks]

for line in lines[stack_end + 2:]:
    line = line.split(' ')
    for i in range(int(line[1])):
        first_stacks[int(line[5]) - 1].append(first_stacks[int(line[3]) - 1].pop())

for line in lines[stack_end + 2:]:
    line = line.split(' ')
    stacks = list()
    for i in range(int(line[1])):
        stacks.append(second_stacks[int(line[3]) - 1].pop())
    stacks.reverse()
    for i in range(len(stacks)):
        second_stacks[int(line[5]) - 1].append(stacks[i])

print(get_message(first_stacks))
print(get_message(second_stacks))
