with open('input.txt') as input_file:
    lines = [line.rstrip() for line in input_file]

calorie_sums = list()

calorie_sum = 0
for line in lines:
    if line == "":
        calorie_sums.append(calorie_sum)
        calorie_sum = 0
    else:
        calorie_sum += int(line)

calorie_sums.sort(reverse=True)

print(calorie_sums[0])
print(sum(calorie_sums[0:2]))
