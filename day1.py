def day_1(filename):
    text = open(filename, 'r')
    lines = text.readlines()

    calibration_sum = 0

    for line in lines:
        numbers = ''
        for element in line:
            if element.isdigit():
                numbers += element
        calibration_value = numbers[0] + numbers[-1]
        calibration_sum += int(calibration_value)

    return calibration_sum


def day_1_part_2(filename):
    valid = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    text = open(filename, 'r')
    lines = text.readlines()

    calibration_sum = 0

    for line in lines:
        numbers = ''
        index = 0
        max_index = len(line) - 1

        while index < max_index:
            if line[index].isalpha():
                found = False
                for name, num in valid.items():
                    if line.find(name, index, max_index) == index:
                        found = True
                        numbers += str(num)
                        index += 1
                        break
                if not found:
                    index += 1
            elif line[index].isdigit():
                numbers += line[index]
                index += 1

        calibration_value = numbers[0] + numbers[-1]
        calibration_sum += int(calibration_value)

    return calibration_sum
