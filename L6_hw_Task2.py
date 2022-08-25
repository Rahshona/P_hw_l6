class Road:
    _length = float or int
    _width = float or int
    weight = float or int
    tickness = float or int

    def __init__(self, length: [int, float], width: [int, float]):
        self._length = float(length)
        self._width = float(width)
        self.mass_a = self._length * self._width


    def value(self):
        self.weight = 25
        self.tickness = 5 / 100
        value = self.mass_a * self.weight * self.tickness / 1000
        print(f'Our result is {value}')
        return 'Good job!'



result = Road(20, 5000)
print(result.value())
