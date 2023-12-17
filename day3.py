def day_3(filename):
    # schematic_sum = 0

    text = open(filename, 'r')
    lines = text.readlines()

    matrix = []

    for line in lines:
        line = line.strip()
        arr_line = []
        for char in line:
            arr_line.append(char)

        matrix.append(arr_line)

    for row in matrix:
        print(row)

    # create a scratch matrix

    # for row in matrix:
    #     for char in row:
    #         # if it's a number, and it's adjacent to a symbol, then mark it as ok

    # go through the scratch matrix and group together all adjacent numbers
    # eww

    # go through the array
    # if it's a number, check if there's an adjacency, and mark it if it is
    # go through again and group together successive numbers together
    # if any of the grouped numbers have adjacencies, add to the schematic

    # return schematic_sum

    return "not done"


def day_3_part_2(filename):
    return "not done"
