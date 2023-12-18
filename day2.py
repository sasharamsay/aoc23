class Game:
    def __init__(self, game_input):
        game = game_input.rstrip()
        pre = game.index(' ')
        post = game.index(':')
        self.number = int(game[pre: post])

        self.contents = game_input.rstrip()[post+2:].split(';')

        roll_list = []

        for roll in self.contents:
            roll_list.append([color.strip() for color in roll.rstrip().split(',')])

        max_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for roll in roll_list:
            for color in roll:
                num_cubes = int(color.split(' ')[0])
                cubes_color = color.split(' ')[1].strip()
                if num_cubes > max_cubes[cubes_color]:
                    max_cubes[cubes_color] = num_cubes

        self.max_cubes = max_cubes

        self.power = max_cubes['red'] * max_cubes['green'] * max_cubes['blue']


def day_2(filename):
    num_red = 12
    num_green = 13
    num_blue = 14
    possible = []

    for line in open(filename, 'r').readlines():
        game = Game(line)

        if game.max_cubes['red'] <= num_red and game.max_cubes['green'] <= num_green and game.max_cubes['blue'] <= num_blue:
            # print('Game ' + str(game.number) + ' is possible!')
            possible.append(game.number)

    return sum(possible)


def day_2_part_2(filename):
    power_sum = 0

    for line in open(filename, 'r').readlines():
        game = Game(line)
        power_sum += game.power

    return power_sum
