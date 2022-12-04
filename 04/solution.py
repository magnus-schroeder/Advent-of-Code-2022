with open('input.txt') as input_file:
    lines = [line.rstrip() for line in input_file]

lines = list(map(lambda x: list(map(lambda y: y.split('-'), x.split(','))), lines))

first_counter = 0
second_counter = 0
for line in lines:
    (first_start, first_end) = line[0]
    (second_start, second_end) = line[1]

    first_set = set(range(int(first_start), int(first_end) + 1))
    second_set = set(range(int(second_start), int(second_end) + 1))

    if first_set.issubset(second_set) or second_set.issubset(first_set):
        first_counter += 1

    if not first_set.isdisjoint(second_set):
        second_counter += 1

print(first_counter)
print(second_counter)
