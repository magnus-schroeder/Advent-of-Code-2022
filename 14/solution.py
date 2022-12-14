import copy

with open('input.txt') as input_file:
    lines = [[line.split(',') for line in line.rstrip().split(' -> ')] for line in input_file]


def solve(cave_og, task_1):
    cave = copy.deepcopy(cave_og)
    count = 0
    while True:
        j, i = 500 - min_x, 0
        for _ in range(max_y):
            if cave[i + 1][j] == '.':
                i += 1
            elif cave[i + 1][j - 1] == '.':
                i += 1
                j -= 1
            elif cave[i + 1][j + 1] == '.':
                i += 1
                j += 1
            else:
                break

        if i == max_y - 1 and task_1:
            return count

        cave[i][j] = 'o'
        count += 1

        if j == 500 - min_x and i == 0 and not task_1:
            return count


max_y = 0
for line in lines:
    for point in line:
        max_y = int(point[1]) if int(point[1]) >= max_y else max_y

max_y += 2
min_x = 500 - max_y
max_x = 500 + max_y

cave = [['.' for j in range(min_x, max_x + 1)] for i in range(max_y)] + [['#' for i in range(min_x, max_x + 1)]]

for line in lines:
    for i in range(len(line) - 1):
        x_1, y_1 = int(line[i][0]), int(line[i][1])
        x_2, y_2 = int(line[i + 1][0]), int(line[i + 1][1])
        for j in range(y_1, y_2 + 1) if y_2 >= y_1 else range(y_2, y_1 + 1):
            for k in range(x_1 - min_x, x_2 - min_x + 1) if x_2 >= x_1 else range(x_2 - min_x, x_1 - min_x + 1):
                cave[j][k] = '#'

print(solve(cave, True))
print(solve(cave, False))
