# Interpolacja Lagrange'a dla węzłów Czebyszewa

import math
import matplotlib.pyplot as pyplot
import numpy as np

from collections import namedtuple
from math import sin, cos, pi
from sklearn import metrics

Point = namedtuple('Point', 'x y')


class Lagrange:
    def __init__(self, points):
        self.n = len(points)
        self.points = points

    def mul(self, x, j):
        b = [(x - self.points[m].x) / (self.points[j].x - self.points[m].x)
             for m in range(self.n) if m != j]
        return np.prod(b, axis=0) * self.points[j].y

    def interpolate(self, x):
        b = [self.mul(x, j) for j in range(self.n)]
        return np.sum(b, axis=0)


class Function:
    def __init__(self, calc):
        self.__calc = calc

    def __call__(self, x):
        return self.__calc(x)


def draw_function(lagrange, function, a, b, interpolation_nodes):
    a = min(math.floor(a), math.ceil(a))
    b = max(math.floor(b), math.ceil(b))
    x = np.linspace(a, b, 100)

    figure = pyplot.figure()
    axis = figure.add_subplot(1, 1, 1)
    axis.spines['right'].set_color('none')
    axis.spines['top'].set_color('none')
    axis.xaxis.set_ticks_position('bottom')
    axis.spines['bottom'].set_position(('data', 0))
    axis.yaxis.set_ticks_position('left')
    axis.spines['left'].set_position(('data', 0))

    axis.plot(1, 0, ls="", marker=">", ms=10, color="k",
              transform=axis.get_yaxis_transform(), clip_on=False)
    axis.plot(0, 1, ls="", marker="^", ms=10, color="k",
              transform=axis.get_xaxis_transform(), clip_on=False)

    y_vals = x.copy()
    for i in range(len(y_vals)):
        y_vals[i] = function(x[i])
    pyplot.plot(x, y_vals, 'r', label="Oryginalna funkcja")

    y_inter_vals = y_vals.copy()
    for i in range(len(y_inter_vals)):
        y_inter_vals[i] = lagrange.interpolate(x[i])

    pyplot.plot(x, y_inter_vals, 'b', linestyle=":", label="Interpolacja funkcji")

    for node in interpolation_nodes:
        pyplot.plot(node.x, function(node.x), 'rx')

    r2 = round(100 * metrics.r2_score(y_vals, y_inter_vals), 3)
    if r2 < 0:
        r2 = 0
    pyplot.title("Dokładność interpolacji: " + str(r2) + "%")

    pyplot.xticks(np.arange(min(x), max(x) + 1, 1.0))
    pyplot.legend()
    pyplot.show()


# obliczanie wezlow Czebyszewa
def calculate_nodes(number_of_nodes, a, b, function):
    nodes = []
    for i in range(0, number_of_nodes):
        x = cos(pi * (2 * i + 1) / (2 * number_of_nodes + 1))
        x = (((b - a) * x) + (a + b)) / 2

        nodes.append(Point(x, function(x)))
    return nodes


def main():
    functions = [
        ("2x + 2", Function(lambda x: 2 * x + 2)),
        ("|x|", Function(lambda x: abs(x))),
        ("x^2", Function(lambda x: x * x)),
        ("sin(x)", Function(lambda x: sin(x))),
        ("2x + 2 + |x|", Function(lambda x: 2 * x + 2 + abs(x))),
        ("x^2 + 2x + 2", Function(lambda x: x * x + 2 * x + 2)),
        ("2x + 2 + sin(x)", Function(lambda x: 2 * x + 2 + sin(x))),
        ("x^2 + |x|", Function(lambda x: x * x + abs(x))),
        ("|x| + sin(x)", Function(lambda x: abs(x) + sin(x))),
        ("x^2 + sin(x)", Function(lambda x: x * x + sin(x)))
    ]

    func_choice = None
    while func_choice is None:
        print("Wybierz funkcje:")
        for i in range(len(functions)):
            print(f"\t{i + 1}. {functions[i][0]}")
        func_choice = input("\t\t>>> ")
        if int(func_choice) not in range(1, len(functions) + 1):
            print("Nie ma takiej opcji w menu")
            func_choice = None
    print("Podaj dolny przedział funkcji")
    a = input("\t\t>>> ")
    b = a
    while b <= a:
        print("Podaj górny przedział funkcji")
        b = input("\t\t>>> ")
    number_of_nodes = 0
    while int(number_of_nodes) <= 0:
        print("Podaj ilość węzłów interpolacyjnych")
        number_of_nodes = input("\t\t>>> ")

    chosen_function = functions[int(func_choice) - 1][1]
    interpolation_nodes = calculate_nodes(int(number_of_nodes), float(a), float(b), chosen_function)

    draw_function(Lagrange(interpolation_nodes), chosen_function, int(a), int(b), interpolation_nodes)


if __name__ == "__main__":
    main()
