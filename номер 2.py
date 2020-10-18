class Road:
    def v(self, _length, _width, m, t):
        self._length = _length
        self._width = _width
        v = (self._length * self._width * m * t)/1000
        print('%sм * %sм * %sкг * %sсм = %sт' % (_length, _width, m, t, v))

l = float(input('Введите длину асфальта: '))
w = float(input('Введите ширину асфальта: '))
m = float(input('Введите массу покрытия 1 кв метра асфальта: '))
t = float(input('Введите толщину асфальта: '))

d = Road()

d.v(l, w, m, t)