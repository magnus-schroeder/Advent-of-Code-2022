import string

with open('input.txt') as input_file:
    lines = [line.rstrip() for line in input_file]


def get_priority(item):
    if item.islower():
        return string.ascii_lowercase.index(item) + 1
    else:
        return string.ascii_uppercase.index(item) + 27


first_priority_sum = 0
second_priority_sum = 0
for i in range(len(lines)):
    line = lines[i]
    firstComp = line[:len(line) // 2]
    secondComp = line[len(line) // 2:]

    first_match = str(list(filter(lambda s: s in secondComp, firstComp)).pop())
    first_priority_sum += get_priority(first_match)

    if i % 3 == 0:
        secondElf = lines[i + 1]
        thirdElf = lines[i + 2]

        second_match = str(list(filter(lambda s: s in secondElf and s in thirdElf, line)).pop())
        second_priority_sum += get_priority(second_match)

print(first_priority_sum)
print(second_priority_sum)
