from math import floor

with open("./day1input.txt") as day1_input:
    modules = [int(EachLine.rstrip()) for EachLine in day1_input]


def additional_fuel(fuel, required_fuel): # This function only for Part 2, Part 1 is solved in the sum() function below
    module_fuel = floor(fuel / 3) - 2

    if module_fuel > 0:
        required_fuel += module_fuel
        return additional_fuel(module_fuel, required_fuel)

    else:
        return required_fuel


Part1 = sum(floor(EachModule / 3) - 2 for EachModule in modules)
Part2 = sum(additional_fuel(EachModule, 0) for EachModule in modules)

print(f"Part 1: {Part1}")
print(f"Part 2: {Part2}")

# Part 1: 3434390
# Part 2: 5148724
