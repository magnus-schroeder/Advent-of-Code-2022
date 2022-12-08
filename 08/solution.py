with open('input.txt') as input_file:
    lines = [[int(char) for char in line.rstrip()] for line in input_file]

visible_trees = set()
tree_scores = list()
for i in range(len(lines)):
    for j in range(len(lines[0])):
        current_tree = lines[i][j]
        current_score = 1

        if 0 < i < len(lines) - 1 or 0 < j < len(lines[0]):
            visible = True
            for k in reversed(range(i)):
                if lines[k][j] >= current_tree:
                    current_score *= i - k
                    visible = False
                    break
            if visible:
                current_score *= i
                visible_trees.add((i, j))

            visible = True
            for l in range(i + 1, len(lines)):
                if lines[l][j] >= current_tree:
                    current_score *= l - i
                    visible = False
                    break
            if visible:
                current_score *= len(lines) - i - 1
                visible_trees.add((i, j))

            visible = True
            for m in reversed(range(j)):
                if lines[i][m] >= current_tree:
                    current_score *= j - m
                    visible = False
                    break
            if visible:
                current_score *= j
                visible_trees.add((i, j))

            visible = True
            for n in range(j + 1, len(lines[0])):
                if lines[i][n] >= current_tree:
                    current_score *= n - j
                    visible = False
                    break
            if visible:
                current_score *= len(lines[0]) - j - 1
                visible_trees.add((i, j))

            tree_scores.append(current_score)
        else:
            visible_trees.add((i, j))

print(len(visible_trees))
print(sorted(tree_scores, reverse=True)[0])
