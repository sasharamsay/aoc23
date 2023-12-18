import math
import re


def get_range(race_time, distance_to_beat):
    # button_press_time * (race_time - button_press_time) = distance_traveled
    # x * (time - x) = dist

    # so in a 7 millisecond race:
    # 1 * (7 - 1) = 6mm

    # eww math
    # x * (time - x) = dist
    # (x * time) - x^2 = dist
    # (x * time) = x^2 + dist
    # y = x^2 - (x * time) + dist

    # quadratic formula:
    # y = ax^2 + bx + c

    # a = 1
    # b = 0 - race_time
    # c = distance to beat

    a = 1
    b = 0 - race_time
    c = distance_to_beat

    min_time_raw = ((0 - b) - (math.sqrt(pow(b, 2) - 4 * a * c))) / (2 * a)
    max_time_raw = ((0 - b) + (math.sqrt(pow(b, 2) - 4 * a * c))) / (2 * a)

    if min_time_raw.is_integer():
        min_time = min_time_raw + 1
    else:
        min_time = math.ceil(min_time_raw)

    if max_time_raw.is_integer():
        max_time = max_time_raw - 1
    else:
        max_time = math.floor(max_time_raw)

    ways_to_win = 0

    for i in range(int(min_time), int(max_time) + 1):
        ways_to_win += 1

    return ways_to_win


def day_6(filename):
    lines = open(filename, 'r').readlines()

    times_init = lines[0].split(':')[1]
    times = re.split("\s+", times_init)

    for t in times:
        if t == '':
            times.remove(t)

    records_init = lines[1].split(':')[1]
    records = re.split("\s+", records_init)

    for r in records:
        if r == '':
            records.remove(r)

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
        if not char.isspace():
            time += char

    for char in records_init:
        if not char.isspace():
            record += char

    return get_range(int(time), int(record))