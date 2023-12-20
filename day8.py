def get_map(lines):
    desert_map = {}

    lines.pop(0)
    lines.remove('\n')

    for line in lines:
        key = line.split('=')[0].rstrip()
        value = line.split('=')[1].rstrip()
        for char in ['(', ')', ' ']:
            value = value.replace(char, '')
        values = value.split(',')
        for val in values:
            val.strip()
        desert_map.update({key: values})

    return desert_map


def a_to_z(start, instructions, full_map, part):
    at_z = False
    pos = start
    steps = 0

    while not at_z:
        for char in instructions:
            steps += 1
            pos = full_map[pos][0] if char == 'L' else full_map[pos][1]
            if part == 1:
                if pos == 'ZZZ':
                    at_z = True
            if part == 2:
                if pos[-1] == 'Z':
                    at_z = True

    return steps


def day_8(filename):
    lines = open(filename, 'r').readlines()
    instructions = lines[0].rstrip()

    desert_map = get_map(lines)

    return a_to_z('AAA', instructions, desert_map, 1)


def lcm(a, b):
    bigger = max(a, b)
    smaller = min(a, b)
    multiplier = bigger

    while multiplier % smaller != 0:
        multiplier += bigger

    return multiplier


def get_end(all_steps):  # get place where all paths sync up and stop at Z, basically the LCM between all path lengths
    a = all_steps[0]
    for i in range(1, len(all_steps)):
        a = lcm(a, all_steps[i])
    return a


def day_8_part_2(filename):
    lines = open(filename, 'r').readlines()
    instructions = lines[0].rstrip()

    desert_map = get_map(lines)
    a_list = []

    for k, v in desert_map.items():
        if k[-1] == 'A':
            a_list.append(k)

    steps_list = []

    for k in a_list:
        steps = a_to_z(k, instructions, desert_map, 2)
        steps_list.append(steps)

    return get_end(steps_list)
