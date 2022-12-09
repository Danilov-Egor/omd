class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        END = '\033[0'
        START = '\033[1;38;2'
        MOD = 'm'
        return f'{START};{self.r};{self.g};{self.b}{MOD}●{END}{MOD}'

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.r == other.r and self.g == other.g and self.b == other.b
        else:
            print('Given object is not of the class Color')

    def __add__(self, other):
        return str(Color(self.r+other.r, self.g+other.g, self.b+other.b))

    def __hash__(self):
        return hash((self.r, self.g, self.b))

    def __rmul__(self, contrast):
        factor = (259 * (contrast + 255)) / (255 * (259 - contrast))

        red_c = round(factor * (self.r - 128) + 128)
        green_c = round(factor * (self.g - 128) + 128)
        blue_c = round(factor * (self.b - 128) + 128)
        return Color(red_c, green_c, blue_c)

    def __mul__(self, contrast):
        return self.__rmul__(contrast)


print(Color(255, 0, 0))

red = Color(255, 0, 0)
print(red == Color(255, 0, 0))

green = Color(0,255,0)
print(red == green)
print(red == 'g')

print(red + green)

orange1 = Color(255, 165, 0)
orange2 = Color(255, 165, 0)
colors = [orange1, red, green, orange2]
sc = set(colors)
print(sc)

print(red * 0.5)
print(0.5 * red)
