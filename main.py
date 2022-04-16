# Interpolacja Lagrange'a dla węzłów Czebyszewa

from math import cos, pi
import numpy as np


# obliczanie wartości funkcji na podstawie wybranej funkcji i x
def calculate_y(func_choice, x):
    match func_choice:
        case '1':
            return 2 * x + 2


# obliczanie x i y dla wybranej funkcji na przedziale (a, b) z zadanym krokiem
def calculate_function(a, b, func_choice, step=0.01):
    x_list = []
    y_list = []
    for i in np.arange(a, b, step):
        x_list.append(i)
        y_list.append(calculate_y(func_choice, i))
    return x_list, y_list


# obliczanie wezlow Czebyszewa
def calculate_nodes(number_of_nodes, a, b, func_choice):
    nodes_x = []
    nodes_y = []
    for i in range(0, number_of_nodes):
        x = cos(pi * (2 * i + 1) / (2 * number_of_nodes + 1))
        x = (((b - a) * x) + (a + b)) / 2

        nodes_x.append(x)
        nodes_y.append(calculate_y(func_choice, x))
    return nodes_x, nodes_y


# interpolacja Lagrange'a
def interpolation(number_of_nodes, nodes_x, nodes_y, a, b, step=0.01):
    interpolated_x = []
    interpolated_y = []
    for i in np.arange(a, b, step):
        y = 0
        for j in range(0, number_of_nodes):
            helper = nodes_y[j]
            for k in range(0, number_of_nodes):
                if j != k:
                    helper *= ((i - nodes_x[k]) / (nodes_x[j] - nodes_x[k]))
            y += helper
        interpolated_x.append(i)
        interpolated_y.append(y)
    return interpolated_x, interpolated_y


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

    original_func_x, original_func_y = calculate_function(float(a), float(b), func_choice)
    nodes_x, nodes_y = calculate_nodes(int(number_of_nodes), float(a), float(b), func_choice)
    inter_x, inter_y = interpolation(int(number_of_nodes), nodes_x, nodes_y, float(a), float(b))


if __name__ == "__main__":
    main()
