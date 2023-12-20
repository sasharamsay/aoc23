import math
import re


def get_range(race_time, distance_to_beat):
    # button_press_time * (race_time - button_press_time) = distance_traveled
    # x * (time - x) = dist
    # press for 1ms in a 7ms race:
    # 1 * (7 - 1) = 6mm

    # x * (time - x) = dist
    # (x * time) - x^2 = dist
    # (x * time) = x^2 + dist
    # y = x^2 - (x * time) + dist

    # quadratic formula:
    # (-b +/- sqrt(b ^ 2) - (4 * a * c)) / 2 * a
    # where ax^2 + bx + c

    a = 1
    b = 0 - race_time
    c = distance_to_beat

    min_time_raw = ((0 - b) - (math.sqrt(pow(b, 2) - 4 * a * c))) / (2 * a)
    max_time_raw = ((0 - b) + (math.sqrt(pow(b, 2) - 4 * a * c))) / (2 * a)

    min_time = min_time_raw + 1 if min_time_raw.is_integer() else math.ceil(min_time_raw)
    max_time = max_time_raw - 1 if max_time_raw.is_integer() else math.floor(max_time_raw)

    ways_to_win = 0

    for i in range(int(min_time), int(max_time) + 1):
        ways_to_win += 1

    return ways_to_win


def day_6(filename):
    lines = open(filename, 'r').readlines()

    times_init = lines[0].split(':')[1]
    times = re.split("\s+", times_init)
    times = [i for i in times if i != '']

    records_init = lines[1].split(':')[1]
    records = re.split("\s+", records_init)
    records = [i for i in records if i != '']

    product = 1

    for i in range(len(times)):
        product *= get_range(int(times[i]), int(records[i]))

    return product


def day_6_part_2(filename):
    lines = open(filename, 'r').readlines()

    times_init = lines[0].split(':')[1]
    records_init = lines[1].split(':')[1]

    time = record = ''

    for char in times_init:
        time += char if not char.isspace() else ''

    for char in records_init:
        record += char if not char.isspace() else ''

    return get_range(int(time), int(record))
