import re


def manhattan_d(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def blocked_in_row(row):
    blocked = set()

    for line in lines:
        xs, ys, xb, yb = line
        diff = manhattan_d(xs, ys, xb, yb) - abs(row - ys)

        if diff >= 0:
            blocked |= set(range(xs - diff, xs + diff + 1))

    return len(blocked) - 1


def find_distress_beacon_frequency(minimum, maximum):
    solution = set()

    for i, line_a in enumerate(lines):
        xs_a, ys_a, xb_a, yb_a = line_a
        r_a = manhattan_d(xs_a, ys_a, xb_a, yb_a) + 1

        for line_b in lines[i + 1:]:
            xs_b, ys_b, xb_b, yb_b = line_b
            r_b = manhattan_d(xs_b, ys_b, xb_b, yb_b) + 1

            if manhattan_d(xs_a, ys_a, xs_b, ys_b) <= r_a + r_b:
                y1, y2 = (xs_a + ys_a + r_a - xs_b + ys_b + r_b) / 2, (xs_a + ys_a + r_a - xs_b + ys_b - r_b) / 2
                x1, x2 = xs_a + ys_a + r_a - y1, xs_a + ys_a + r_a - y2
                y3, y4 = (-xs_a + ys_a + r_a + xs_b + ys_b + r_b) / 2, (-xs_a + ys_a + r_a + xs_b + ys_b - r_b) / 2
                x3, x4 = xs_a - ys_a - r_a + y3, xs_a - ys_a - r_a + y4
                y5, y6 = (-xs_a + ys_a - r_a + xs_b + ys_b + r_b) / 2, (-xs_a + ys_a - r_a + xs_b + ys_b - r_b) / 2
                x5, x6 = xs_a - ys_a + r_a + y5, xs_a - ys_a + r_a + y6
                y7, y8 = (xs_a + ys_a - r_a - xs_b + ys_b + r_b) / 2, (xs_a + ys_a - r_a - xs_b + ys_b - r_b) / 2
                x7, x8 = xs_a + ys_a - r_a - y7, xs_a + ys_a - r_a - y8

                potential_intersections = {(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7),
                                           (x8, y8)}

                solution |= set(filter(lambda x:
                                       x[0] % 1 == 0 and
                                       x[1] % 1 == 0 and
                                       minimum <= x[0] <= maximum and
                                       minimum <= x[1] <= maximum and
                                       manhattan_d(x[0], x[1], xs_a, ys_a) == r_a and
                                       manhattan_d(x[0], x[1], xs_b, ys_b) == r_b, potential_intersections
                                       ))

    for line in lines:
        xs, ys, xb, yb = line

        solution = set(filter(lambda x: manhattan_d(x[0], x[1], xs, ys) > manhattan_d(xs, ys, xb, yb), solution))

    solution = solution.pop()
    return int(solution[0] * 4000000 + solution[1])


with open('input.txt') as input_file:
    lines = [list(map(lambda x: int(re.sub(r'[^0-9-]', '', x)), re.split(r'[:,]', line))) for line in input_file]

print(blocked_in_row(2000000))
print(find_distress_beacon_frequency(0, 4000000))
