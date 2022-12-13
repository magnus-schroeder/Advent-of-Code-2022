import ast
import functools

with open('input.txt') as input_file:
    lines = [line.rstrip() for line in input_file]


def check_order(packet_a, packet_b):
    for i in range(len(packet_a)):
        try:
            if type(packet_a[i]) is int and type(packet_b[i]) is int:
                if packet_a[i] < packet_b[i]:
                    return 1
                elif packet_a[i] > packet_b[i]:
                    return -1
            elif type(packet_a[i]) is list and type(packet_b[i]) is list:
                check = check_order(packet_a[i], packet_b[i])
                if check != 0:
                    return check
            else:
                packet_a_list = list(packet_a[i]) if type(packet_a[i]) is list else [packet_a[i]]
                packet_b_list = list(packet_b[i]) if type(packet_b[i]) is list else [packet_b[i]]
                check = check_order(packet_a_list, packet_b_list)
                if check != 0:
                    return check
        except IndexError:
            return -1

    if len(packet_a) < len(packet_b):
        return 1
    else:
        return 0


packet_pairs = list()
for i in range(0, len(lines), 3):
    packet_pairs.append((ast.literal_eval(lines[i]), ast.literal_eval(lines[i + 1])))

checked = list()
for i in range(len(packet_pairs)):
    if check_order(packet_pairs[i][0], packet_pairs[i][1]) == 1:
        checked.append(i + 1)

packets = [[[2]], [[6]]]
for packet_pair in packet_pairs:
    packets.append(packet_pair[0])
    packets.append(packet_pair[1])

packets.sort(key=functools.cmp_to_key(check_order), reverse=True)

print(sum(checked))
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
