import string

with open('input.txt') as input_file:
    lines = [line.rstrip() for line in input_file]


def bfs(start, target):
    visited = set()
    count = {start: 0}
    q = list()
    visited.add(start)
    q.append(start)
    
    while q:
        v = q.pop(0)
        if v == target:
            return count[target]

        i, j = v
        v_value = 0
        if lines[i][j].islower():
            v_value = string.ascii_lowercase.index(lines[i][j])

        neighbors = list()
        if i > 0 and (i - 1, j) not in visited and string.ascii_lowercase.index(lines[i - 1][j]) <= v_value + 1:
            neighbors.append((i - 1, j))
        if i + 1 < len(lines) and (i + 1, j) not in visited and string.ascii_lowercase.index(lines[i + 1][j]) <= v_value + 1:
            neighbors.append((i + 1, j))
        if j > 0 and (i, j - 1) not in visited and string.ascii_lowercase.index(lines[i][j - 1]) <= v_value + 1:
            neighbors.append((i, j - 1))
        if j + 1 < len(lines[0]) and (i, j + 1) not in visited and string.ascii_lowercase.index(lines[i][j + 1]) <= v_value + 1:
            neighbors.append((i, j + 1))

        for w in neighbors:
            visited.add(w)
            count[w] = count[v] + 1
            q.append(w)


joined_lines = ''.join(lines)
start_pos = (joined_lines.find('S') // len(lines[0]), joined_lines.find('S') % len(lines[0]))
target_pos = (joined_lines.find('E') // len(lines[0]), joined_lines.find('E') % len(lines[0]))
lines[start_pos[0]] = lines[start_pos[0]][:start_pos[1]] + 'a' + lines[start_pos[0]][start_pos[1] + 1:]
lines[target_pos[0]] = lines[target_pos[0]][:target_pos[1]] + 'z' + lines[target_pos[0]][target_pos[1] + 1:]

trail_lengths = list()
for i in range(len(joined_lines)):
    if joined_lines[i] == 'a':
        count = bfs((i // len(lines[0]), i % len(lines[0])), target_pos)
        if count is not None:
            trail_lengths.append(count)

print(bfs(start_pos, target_pos))
print(min(trail_lengths))
    