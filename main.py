# Interpolacja Lagrange'a dla węzłów Czebyszewa

from math import cos, pi
from collections import namedtuple
import numpy as np

Point = namedtuple('Point', 'x y')

# obliczanie wartości funkcji na podstawie wybranej funkcji i x
def calculate_y(func_choice, x):
    if func_choice == '1':
        return 2 * x + 2


# obliczanie x i y dla wybranej funkcji na przedziale (a, b) z zadanym krokiem
def calculate_function(a, b, func_choice, step=0.01):
    points = []
    for i in np.arange(a, b, step):
        points.append(Point(i, calculate_y(func_choice, i)))
    return points


# obliczanie wezlow Czebyszewa
def calculate_nodes(number_of_nodes, a, b, func_choice):
    nodes = []
    for i in range(0, number_of_nodes):
        x = cos(pi * (2 * i + 1) / (2 * number_of_nodes + 1))
        x = (((b - a) * x) + (a + b)) / 2

        nodes.append(Point(x, calculate_y(func_choice, x)))
    return nodes


# interpolacja Lagrange'a
def interpolation(number_of_nodes, nodes, a, b, step=0.01):
    interpolated_points = []
    for i in np.arange(a, b, step):
        y = 0
        for j in range(0, number_of_nodes):
            helper = nodes[j].y
            for k in range(0, number_of_nodes):
                if j != k:
                    helper *= ((i - nodes[k].x) / (nodes[j].x - nodes[k].x))
            y += helper
        interpolated_points.append(Point(i, y))
    return interpolated_points


def main():
    func_choice = None
    while func_choice is None:
        print("Wybierz funckje")
        print("1. 2x + 2")
        # todo dodac kolejne funkcje i przerobic odpowiednio if nizej
        func_choice = input("\t\t>>> ")
        if int(func_choice) != 1:
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

    #original_func_x, original_func_y = calculate_function(float(a), float(b), func_choice)
    nodes = calculate_nodes(int(number_of_nodes), float(a), float(b), func_choice)
    interpolated_points = interpolation(int(number_of_nodes), nodes, float(a), float(b))
    for point in interpolated_points:
        print(f"x: {point.x}, y: {point.y}")


if __name__ == "__main__":
    main()
