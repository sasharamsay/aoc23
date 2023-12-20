def get_matches(have, winning):
    num_matches = 0

    for h in have:
        for w in winning:
            if h == w and h != '' and w != '':
                num_matches += 1

    return num_matches


def day_4(filename):
    points = 0

    for line in open(filename, 'r').readlines():
        start1 = line.index(':') + 2
        end1 = line.index('|')

        winning = line[start1:end1].strip().split(' ')
        have = line[end1 + 2:].strip().split(' ')

        num_matches = get_matches(have, winning)

        if num_matches == 1:
            points += 1
        if num_matches > 1:
            points += pow(2, num_matches - 1)

    return points


def day_4_part_2(filename):
    lines = open(filename, 'r').readlines()

    frequency = {}

    for count, line in enumerate(lines):
        frequency.update({count: 1})

    for index, line in enumerate(lines):
        start1 = line.index(':') + 2
        end1 = line.index('|')

        winning = line[start1:end1].strip().split(' ')
        have = line[end1 + 2:].strip().split(' ')

        for i in range(frequency[index]):
            num_matches = get_matches(have, winning)
            for m in range(1, num_matches + 1):
                frequency.update({(index + m): (frequency[index + m] + 1)})

    return sum(frequency.values())

