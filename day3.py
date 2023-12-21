def is_symbol(char):
    if not char.isalnum() and char != '.':
        return True
    return False


def get_value(positions, schematic):
    value = ''
    for p in positions:
        value += schematic[p[0]][p[1]]
    return int(value)


def is_part(positions, schematic):
    for row, col in positions:
        chars = []

        if row - 1 >= 0:
            chars.append(schematic[row - 1][col])                       # N
        if row - 1 >= 0 and col + 1 < len(schematic[row]):
            chars.append(schematic[row - 1][col + 1])                   # NE
        if col + 1 < len(schematic[row]) and row - 1 >= 0:
            chars.append(schematic[row][col + 1])                       # E
        if row + 1 < len(schematic) and col + 1 < len(schematic[row]):
            chars.append(schematic[row + 1][col + 1])                   # SE
        if row + 1 < len(schematic):
            chars.append(schematic[row + 1][col])                       # S
        if row + 1 < len(schematic) and col - 1 >= 0:
            chars.append(schematic[row + 1][col - 1])                   # SW
        if col - 1 >= 0:
            chars.append(schematic[row][col - 1])                       # W
        if row - 1 >= 0 and col - 1 >= 0:
            chars.append(schematic[row - 1][col - 1])                   # NW

        for char in chars:
            if is_symbol(char):
                return True

    return False


def day_3(filename):
    schematic_sum = 0
    schematic = []

    for line in open(filename, 'r').readlines():
        schematic.append([str(char) for char in line.strip()])

    numbers = []

    for r, row in enumerate(schematic):
        i = 0
        while i < len(row):
            if i == len(row) - 1:
                break
            if row[i].isdigit():
                number_indices = []
                while row[i].isdigit() and i < len(row) - 1:
                    number_indices.append([r, i])
                    i += 1
                if i == len(row) - 1 and row[i].isdigit():
                    number_indices.append([r, i])
                numbers.append(number_indices)
            else:
                if i < len(row):
                    i += 1

    for n in numbers:
        if is_part(n, schematic):
            schematic_sum += get_value(n, schematic)

    return schematic_sum


def day_3_part_2(filename):
    return "not done"
