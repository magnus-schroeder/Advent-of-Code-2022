with open('input.txt') as input_file:
    lines = [line.rstrip().split(' ') for line in input_file]

tail_positions = [(0, 0) for i in range(10)]
moves_x = {'L': -1, 'R': 1, 'D': 0, 'U': 0}
moves_y = {'L': 0, 'R': 0, 'D': -1, 'U': 1}

first_tail_positions_visited = set()
last_tail_positions_visited = set()

for line in lines:
    direction, steps = line
    for step in range(int(steps)):
        tail_positions[0] = (tail_positions[0][0] + moves_x[direction], tail_positions[0][1] + moves_y[direction])

        for i in range(1, len(tail_positions)):
            tail_x, tail_y = tail_positions[i]
            diff_x = tail_positions[i - 1][0] - tail_x
            diff_y = tail_positions[i - 1][1] - tail_y

            if abs(diff_x) == 2 or abs(diff_y) == 2:
                if abs(diff_x) == 2 and abs(diff_y) == 2:
                    tail_positions[i] = (tail_x + diff_x / 2, tail_y + diff_y / 2)
                elif abs(diff_x) == 2:
                    tail_positions[i] = (tail_x + diff_x / 2, tail_y + diff_y)
                elif abs(diff_y) == 2:
                    tail_positions[i] = (tail_x + diff_x, tail_y + diff_y / 2)

        first_tail_positions_visited.add(tail_positions[1])
        last_tail_positions_visited.add(tail_positions[9])

print(len(first_tail_positions_visited))
print(len(last_tail_positions_visited))
