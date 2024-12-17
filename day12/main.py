"""
Advent of code 2024 day X
https://adventofcode.com/2024/day/X
"""
__author__ = "Conner Beard"

import os
import time
from itertools import product


def load_puzzle_input(file_name):
    """

    Args:
        file_name (ascii text file): puzzle input

    Returns:
    """
    array = []
    with open(file_name, 'r') as file:
        for row in file.readlines():
            array.append(list(row)[:-1])

    return array


def check_bounds(row, col, array):
    """
    check if array indexing is within the bounds of the array
    Args:
        row (int): array row
        col (int): array col
        array (list of lists): array to check bounds on
    Returns:
        (bool): True if in bounds, False if out of bounds
    """
    if (row < 0) | (col < 0):
        return False
    if row > (len(array) - 1):
        return False
    if col > (len(array[0]) - 1):
        return False
    return True


def recursive_plot(farm, crop, row_num, col_num, inside_plot, depth=0):
    inside_plot.add((row_num, col_num))
    depth = depth + 1
    if depth > 1000:
        raise Exception("Hit recursion limit")

    for row_adder, col_adder in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if row_adder == col_adder == 0:
            continue
        target_row = row_num+row_adder
        target_col = col_num+col_adder
        if not check_bounds(target_row, target_col, farm):
            continue

        if ((farm[target_row][target_col] == crop) &
           ((target_row, target_col) not in inside_plot)):
            inside_plot.add((target_row, target_col))
            inside_plot = recursive_plot(farm, crop,
                                         target_row, target_col,
                                         inside_plot, depth)

    return inside_plot


def get_perimeter(plot):
    perimeter = 0
    for tile in plot:
        for row_adder, col_adder in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if row_adder == col_adder == 0:
                continue
            target_row = tile[0] + row_adder
            target_col = tile[1] + col_adder

            if (target_row, target_col) in plot:
                pass
            else:
                perimeter = perimeter + 1

    return perimeter


def get_sides(plot):
    raise Exception("Write Me")


def solve_part_1(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
    """

    checked_tiles = set()
    plots = []

    farm = load_puzzle_input(file_name)

    for row_num, row in enumerate(farm):
        for col_num, crop in enumerate(row):
            if (row_num, col_num) not in checked_tiles:
                new_plot = recursive_plot(farm, crop, row_num, col_num, inside_plot=set())
                for tile in new_plot:
                    checked_tiles.add(tile)
                plots.append(new_plot)

    total_price = 0
    for i in plots:
        price = len(i) * get_perimeter(i)
        total_price = total_price + price

    return total_price


def solve_part_2(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
    """
    checked_tiles = set()
    plots = []

    farm = load_puzzle_input(file_name)

    for row_num, row in enumerate(farm):
        for col_num, crop in enumerate(row):
            if (row_num, col_num) not in checked_tiles:
                new_plot = recursive_plot(farm, crop, row_num, col_num, inside_plot=set())
                for tile in new_plot:
                    checked_tiles.add(tile)
                plots.append(new_plot)

    total_price = 0
    for i in plots:
        price = len(i) * get_sides(i)
        total_price = total_price + price

    return total_price


if __name__ == '__main__':
    test_input_path = os.path.dirname(__file__) + '/test_input.txt'
    input_path = os.path.dirname(__file__) + '/input.txt'

    start = time.time()
    assert solve_part_1(test_input_path) == 1930
    solution_1 = solve_part_1(input_path)
    print(f"Day X part 1 solution: {solution_1}, time:{time.time()-start}")

    start = time.time()
    assert solve_part_2(test_input_path) == 1206
    solution_2 = solve_part_2(input_path)
    print(f"Day X part 2 solution: {solution_2}, time:{time.time()-start}")
