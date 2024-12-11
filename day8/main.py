"""
Advent of code 2024 day 8
https://adventofcode.com/2024/day/8
"""
__author__ = "Conner Beard"

import os
import time
from collections import defaultdict
import itertools


def load_puzzle_input(file_name):
    """
    Read in the crossword puzzle

    Args:
        file_name (ascii text file): puzzle input

    Returns:
        rules (list of list of two int): a list of rules to apply to orders
        to determine if each order is correct

        orders (list of list of int): a list of numbers that may or may not
        follow the ordering guideline in rules
    """
    array = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            row = []
            for value in line[:-1]:
                row.append(value)
            array.append(row)

    return array


def get_frequencies(array):
    unique = defaultdict(list)
    for row_num, row in enumerate(array):
        for col_num, value in enumerate(row):
            if value != '.':
                unique[value].append(((row_num), (col_num)))
    return unique


def find_antinodes(a, b):
    x_slope = b[0] - a[0]
    y_slope = b[1] - a[1]

    antinode1 = (a[0] - x_slope, a[1] - y_slope)
    antinode2 = (b[0] + x_slope, b[1] + y_slope)

    return antinode1, antinode2


def find_antinodes_and_resonance(a, b):
    antinodes = []
    antinodes.append(a)
    antinodes.append(b)

    x_slope = b[0] - a[0]
    y_slope = b[1] - a[1]

    for distance in range(1, 1000):
        antinodes.append((a[0] - (x_slope*distance), a[1] - (y_slope*distance)))
        antinodes.append((b[0] + (x_slope*distance), b[1] + (y_slope*distance)))

    return antinodes


def check_inside_bounds(array, values):
    output = set()
    row_min = 0
    row_max = len(array) - 1
    col_min = 0
    col_max = len(array[0]) - 1
    for value in values:
        if value[0] < row_min:
            continue
        if value[0] > row_max:
            continue
        if value[1] < col_min:
            continue
        if value[1] > col_max:
            continue
        output.add(value)

    return output


def solve_part_1(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the sum of middle values in the correct orders in the puzzle input
    """
    array = load_puzzle_input(file_name)
    frequecies = get_frequencies(array)

    antinodes = []
    for key, value in frequecies.items():
        for antenna_1, antenna_2 in itertools.combinations(value, 2):
            antinodes = antinodes + [*find_antinodes(antenna_1, antenna_2)]

    antinodes = check_inside_bounds(array, antinodes)

    return len(antinodes)


def solve_part_2(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the sum of middle values in the incorrect orders in the puzzle input
        once they have been re-ordered to be correct
    """
    array = load_puzzle_input(file_name)
    frequencies = get_frequencies(array)

    antinodes = []
    for key, value in frequencies.items():
        if len(value) == 1:
            continue
        for antenna_1, antenna_2 in itertools.combinations(value, 2):
            antinodes = antinodes + find_antinodes_and_resonance(antenna_1, antenna_2)

    antinodes = check_inside_bounds(array, antinodes)

    return len(antinodes)


if __name__ == '__main__':
    test_input_path = os.path.dirname(__file__) + '/test_input.txt'
    input_path = os.path.dirname(__file__) + '/input.txt'

    start = time.time()
    assert solve_part_1(test_input_path) == 14
    solution_1 = solve_part_1(input_path)
    print(f"Day 8 part 1 solution: {solution_1}, time:{time.time()-start}")

    start = time.time()
    assert solve_part_2(test_input_path) == 34
    solution_2 = solve_part_2(input_path)
    print(f"Day 8 part 2 solution: {solution_2}, time:{time.time()-start}")
