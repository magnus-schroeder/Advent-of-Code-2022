import copy
import math
import operator

with open('input.txt') as input_file:
    lines = [line.rstrip() for line in input_file]

monkeys = list()
for i in range(0, len(lines), 7):
    monkey = dict()
    monkey['items'] = [int(el) for el in lines[i + 1].replace(',', '').split(' ')[4:]]
    operation_line = lines[i + 2].split(' ')
    if operation_line[6] == '+':
        monkey['operator'] = operator.add
    elif operation_line[6] == '*':
        monkey['operator'] = operator.mul
    monkey['value'] = operation_line[7]
    monkey['test'] = int(lines[i + 3].split(' ')[5])
    monkey['true'] = int(lines[i + 4].split(' ')[9])
    monkey['false'] = int(lines[i + 5].split(' ')[9])
    monkeys.append(monkey)

test_factor = math.prod([monkey['test'] for monkey in monkeys])


def monkey_business(monkeys_og, worry_level_factor, rounds):
    monkeys = copy.deepcopy(monkeys_og)
    inspections = [0 for i in range(len(monkeys))]
    for i in range(rounds):
        for monkey_i, monkey in enumerate(monkeys):
            for item in monkey['items']:
                worry_level = item

                if monkey['value'] == 'old':
                    worry_level = monkey['operator'](worry_level, worry_level) // worry_level_factor % test_factor
                else:
                    worry_level = monkey['operator'](worry_level, int(monkey['value'])) // worry_level_factor % test_factor
                inspections[monkey_i] += 1
                if worry_level % monkey['test'] == 0:
                    monkeys[monkey['true']]['items'].append(worry_level)
                else:
                    monkeys[monkey['false']]['items'].append(worry_level)

            monkeys[monkey_i]['items'].clear()

    return math.prod(sorted(inspections, reverse=True)[:2])


print(monkey_business(monkeys, 3, 20))
print(monkey_business(monkeys, 1, 10000))
