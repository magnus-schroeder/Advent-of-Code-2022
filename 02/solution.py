import string

with open('input.txt') as input_file:
    lines = [line.rstrip() for line in input_file]

score_1 = 0
score_2 = 0
for line in lines:
    opponent_move = string.ascii_uppercase.index(line[0])
    my_move = string.ascii_uppercase.index(line[2]) - 23

    if (my_move - opponent_move) % 3 == 1:
        score_1 += my_move + 7
    elif my_move == opponent_move:
        score_1 += my_move + 4
    else:
        score_1 += my_move + 1

    if my_move == 0:
        score_2 += (opponent_move - 1) % 3 + 1
    elif my_move == 1:
        score_2 += opponent_move + 4
    else:
        score_2 += (opponent_move + 1) % 3 + 7

print(score_1)
print(score_2)
