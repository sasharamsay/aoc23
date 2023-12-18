def get_map(lines, map_name):
    ret_map = []
    for count, line in enumerate(lines):
        if line.startswith(map_name):
            i = 1
            while lines[count + i] != '\n':
                ret_map.append(lines[count + i].strip().split(' '))
                i += 1
                if count + i == len(lines):
                    break
    return ret_map


def translate(curr_input, curr_map):
    output = []
    out = -1
    for curr in curr_input:
        for index, option in enumerate(curr_map):

            min_destination = int(option[0])
            max_destination = int(option[0]) + int(option[2])
            # print("min destination: " + str(min_destination) + " max destination: " + str(max_destination))

            min_source = int(option[1])
            max_source = int(option[1]) + int(option[2])
            # print("min source: " + str(min_source) + " max source: " + str(max_source))

            out = -1

            if min_source <= int(curr) <= max_source:
                # print("input " + str(curr) + " is in range " + str(min_source) + " to " + str(max_source))
                out = min_destination + (int(curr) - min_source)
                # print("Soil is " + str(out))
                output.append(out)
                break

        if out == -1:
            # print("No match. output is " + str(curr))
            output.append(curr)
    # print(output)
    return output


def day_5(filename):
    lines = open(filename, 'r').readlines()

    seeds = []
    seed_to_soil = get_map(lines, 'seed-to-soil')
    soil_to_fertilizer = get_map(lines, 'soil-to-fertilizer')
    fertilizer_to_water = get_map(lines, 'fertilizer-to-water')
    water_to_light = get_map(lines, 'water-to-light')
    light_to_temperature = get_map(lines, 'light-to-temperature')
    temperature_to_humidity = get_map(lines, 'temperature-to-humidity')
    humidity_to_location = get_map(lines, 'humidity-to-location')

    for count, line in enumerate(lines):
        if line.startswith('seeds:'):
            # print(line)
            seeds = line[line.index(':') + 1:].strip().split(' ')
            # print(seeds)

    soil = (translate(seeds, seed_to_soil))
    fertilizer = translate(soil, soil_to_fertilizer)
    water = translate(fertilizer, fertilizer_to_water)
    light = translate(water, water_to_light)
    temperature = translate(light, light_to_temperature)
    humidity = translate(temperature, temperature_to_humidity)
    location = translate(humidity, humidity_to_location)

    return min(location)


def day_5_part_2(filename):
    lines = open(filename, 'r').readlines()

    seeds = []
    seed_to_soil = get_map(lines, 'seed-to-soil')
    soil_to_fertilizer = get_map(lines, 'soil-to-fertilizer')
    fertilizer_to_water = get_map(lines, 'fertilizer-to-water')
    water_to_light = get_map(lines, 'water-to-light')
    light_to_temperature = get_map(lines, 'light-to-temperature')
    temperature_to_humidity = get_map(lines, 'temperature-to-humidity')
    humidity_to_location = get_map(lines, 'humidity-to-location')

    for count, line in enumerate(lines):
        if line.startswith('seeds:'):
            # print(line)
            seeds = line[line.index(':') + 1:].strip().split(' ')
            # print(seeds)

    more_seeds = []

    ranges = {}

    i = 0
    while i < len(seeds):
        more_seeds.append(int(seeds[i]))
        more_seeds.append(int(seeds[i]) + int(seeds[i + 1]))
        ranges.update({int(seeds[i]): int(seeds[i]) + int(seeds[i + 1])})
        i += 2

    # print("ranges: " + str(ranges))
    # print("more seeds: " + str(more_seeds))

    soil = (translate(more_seeds, seed_to_soil))
    fertilizer = translate(soil, soil_to_fertilizer)
    water = translate(fertilizer, fertilizer_to_water)
    light = translate(water, water_to_light)
    temperature = translate(light, light_to_temperature)
    humidity = translate(temperature, temperature_to_humidity)
    location = translate(humidity, humidity_to_location)

    # print("location: " + str(location))

    # return min(location)

    return "not done"
