from day1 import *
from day2 import *
from day3 import *
from day4 import *
from day5 import *
from day6 import *
from day7 import *


def run(day, part):
    filename = "input/in" + str(day) + ".txt"
    match day:
        case 1:
            print(day_1(filename)) if part == 1 else print(day_1_part_2(filename))
        case 2:
            print(day_2(filename)) if part == 1 else print(day_2_part_2(filename))
        case 3:
            print(day_3(filename)) if part == 1 else print(day_3_part_2(filename))
        case 4:
            print(day_4(filename)) if part == 1 else print(day_4_part_2(filename))
        case 5:
            print(day_5(filename)) if part == 1 else print(day_5_part_2(filename))
        case 6:
            print(day_6(filename)) if part == 1 else print(day_6_part_2(filename))
        case 7:
            print(day_7(filename)) if part == 1 else print(day_7_part_2(filename))
        case _:
            print("Day " + str(day) + " isn't done.")


if __name__ == '__main__':
    day_input = int(input("Day: "))
    part_input = int(input("Part: "))
    run(day_input, part_input)


