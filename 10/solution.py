with open('input.txt') as input_file:
    lines = [line.rstrip().split(' ') for line in input_file]

signals = list()
crt = [['.' for j in range(40)] for i in range(6)]
cycle = 0
x = 1


def update():
    global cycle
    local_row = ['.' for i in range(40)]
    cycle += 1

    if 0 <= x <= 39:
        row = (cycle - 1) // 40
        col = (cycle - 1) % 40

        local_row[x] = '#'
        if 0 <= x - 1 <= 39:
            local_row[x - 1] = '#'
        if 0 <= x + 1 <= 39:
            local_row[x + 1] = '#'

        crt[row][col] = local_row[col]

    signals.append(cycle * x)


for line in lines:
    update()
    if line[0] == 'addx':
        update()
        x += int(line[1])

print(sum([signals[i - 1] for i in [20, 60, 100, 140, 180, 220]]))
for row in crt:
    print(''.join(row))
