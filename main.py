from day1 import *
from day2 import *
from day3 import *
from day4 import *
from day5 import *
from day6 import *
from day7 import *
from day8 import *
from day9 import *


def run(day, part):
    filename = "input/in" + str(day) + ".txt"

    day_map = {
        1: (day_1, day_1_part_2),
        2: (day_2, day_2_part_2),
        3: (day_3, day_3_part_2),
        4: (day_4, day_4_part_2),
        5: (day_5, day_5_part_2),
        6: (day_6, day_6_part_2),
        7: (day_7, day_7_part_2),
        8: (day_8, day_8_part_2),
        9: (day_9, day_9_part_2)
    }

    print(day_map[day][part-1](filename))


if __name__ == '__main__':
    day_input = int(input("Day: "))
    part_input = int(input("Part: "))
    run(day_input, part_input)
