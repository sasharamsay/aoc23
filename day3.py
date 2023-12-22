class Schematic:
    def __init__(self, text):
        self.stars = {}
        self.content = self.get_content(text)
        self.parts = self.get_parts()

    def get_content(self, text):
        content = []
        for line in text:
            content.append([str(char) for char in line.strip()])
        return content

    def get_parts(self):
        parts = []

        for r, row in enumerate(self.content):
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
                    parts.append(Part(number_indices, self.content))
                else:
                    if i < len(row):
                        i += 1
        return parts

    def __str__(self):
        output = ''
        for line in self.content:
            output += str(line) + '\n'

        for part in self.parts:
            output += str(part) + '\n'
        return output

    __repr__ = __str__


class Symbol:
    def __init__(self, char, position, part):
        self.char = char
        self.position = position
        self.next_to = part

    def is_valid_symbol(self):
        if not self.char.isalnum() and self.char != '.':
            return True
        return False

    def is_star(self):
        return self.char == '*'

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(str(self.char) + str(self.position))

    def __str__(self):
        output = ''
        output += str(self.char) + " at " + str(self.position)
        return output

    __repr__ = __str__


class Part:
    def __init__(self, positions, schematic):
        self.schematic = schematic
        self.positions = positions
        self.adjacent = []
        self.is_part = self.get_is_part()
        self.value = self.get_value()

    def get_is_part(self):
        for row, col in self.positions:
            if row - 1 >= 0:
                temp = Symbol(self.schematic[row - 1][col], [row - 1, col], self)
                if not temp.char.isdigit() and temp not in self.adjacent:
                    self.adjacent.append(temp)                                                      # N
            if row - 1 >= 0 and col + 1 < len(self.schematic[row]):
                temp = Symbol(self.schematic[row - 1][col + 1], [row - 1, col + 1], self)
                if not temp.char.isdigit() and temp not in self.adjacent:
                    self.adjacent.append(temp)                                                      # NE
            if col + 1 < len(self.schematic[row]):
                temp = Symbol(self.schematic[row][col + 1], [row, col + 1], self)
                if not temp.char.isdigit() and temp not in self.adjacent:
                    self.adjacent.append(temp)                                                      # E
            if row + 1 < len(self.schematic) and col + 1 < len(self.schematic[row]):
                temp = Symbol(self.schematic[row + 1][col + 1], [row + 1, col + 1], self)
                if not temp.char.isdigit() and temp not in self.adjacent:
                    self.adjacent.append(temp)                                                      # SE
            if row + 1 < len(self.schematic):
                temp = Symbol(self.schematic[row + 1][col], [row + 1, col], self)
                if not temp.char.isdigit() and temp not in self.adjacent:
                    self.adjacent.append(temp)                                                      # S
            if row + 1 < len(self.schematic) and col - 1 >= 0:
                temp = Symbol(self.schematic[row + 1][col - 1], [row + 1, col - 1], self)
                if not temp.char.isdigit() and temp not in self.adjacent:
                    self.adjacent.append(temp)                                                      # SW
            if col - 1 >= 0:
                temp = Symbol(self.schematic[row][col - 1], [row, col - 1], self)
                if not temp.char.isdigit() and temp not in self.adjacent:
                    self.adjacent.append(temp)                                                      # W
            if row - 1 >= 0 and col - 1 >= 0:
                temp = Symbol(self.schematic[row - 1][col - 1], [row - 1, col - 1], self)
                if not temp.char.isdigit() and temp not in self.adjacent:
                    self.adjacent.append(temp)                                                      # NW
            for char in self.adjacent:
                if char.is_valid_symbol():
                    return True
        return False

    def get_value(self):
        value = ''
        for p in self.positions:
            value += self.schematic[p[0]][p[1]]
        return int(value)

    def __str__(self):
        output = ''
        output += str(self.positions) + '\n' + str(self.value) + '\n' + str(self.is_part) + '\n'
        for char in self.adjacent:
            output += str(char) + '\n'
        return output

    __repr__ = __str__


def day_3(filename):
    schematic = Schematic(open(filename, 'r').readlines())
    schematic_sum = 0

    for part in schematic.parts:
        if part.is_part:
            schematic_sum += part.value

    return schematic_sum


def day_3_part_2(filename):
    schematic = Schematic(open(filename, 'r').readlines())

    star_map = {}

    for part in schematic.parts:
        if part.is_part:
            for symbol in part.adjacent:
                pos = str(symbol.position)
                if pos in star_map:
                    if part.get_value() not in star_map[pos]:
                        star_map[pos].append(part.get_value())
                elif symbol.is_star():
                    star_map.update({pos: [part.get_value()]})

    product_sum = 0

    for k, v in star_map.items():
        if len(v) == 2:
            product_sum += v[0] * v[1]

    return product_sum
