from itertools import product

with open("./day2input.txt") as day2_input:
    input_string = day2_input.readline()
    intcode = [int(x) for x in input_string.split(",")]


def instruction(inst_pointer, input_one, input_two):
    if inst_pointer == 1:
        return input_one + input_two
    elif inst_pointer == 2:
        return input_one * input_two


opcode = 0

# Part 1-------------------------
part1_list = intcode[:]
part1_list[1] = 12
part1_list[2] = 2

while part1_list[opcode] != 99:
    overwrite = part1_list[opcode + 3]  # Storing in variables for readability
    position1 = part1_list[opcode + 1]
    position2 = part1_list[opcode + 2]

    part1_list[overwrite] = instruction(part1_list[opcode], part1_list[position1], part1_list[position2])
    opcode += 4

# Part 2-------------------------
part2_list = intcode[:]
nounverbs = list(product(range(0, 100), repeat=2))
pointer = 0

while pointer < len(nounverbs):
    part2_list = intcode[:]
    opcode = 0
    part2_list[1] = nounverbs[pointer][0]
    part2_list[2] = nounverbs[pointer][1]

    while part2_list[opcode] != 99:
        overwrite = part2_list[opcode + 3]
        position1 = part2_list[opcode + 1]
        position2 = part2_list[opcode + 2]

        part2_list[overwrite] = instruction(part2_list[opcode], part2_list[position1], part2_list[position2])
        opcode += 4

    if part2_list[0] == 19690720:
        break
    else:
        pointer += 1


Part1 = part1_list[0]
Part2 = (100 * nounverbs[pointer][0]) + nounverbs[pointer][1]

print(f"Part 1: {Part1}")
print(f"Part 2: {Part2}")

# Part 1: 4090701
# Part 2: 6421
