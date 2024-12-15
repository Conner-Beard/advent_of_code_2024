"""
Advent of code 2024 day X
https://adventofcode.com/2024/day/X
"""
__author__ = "Conner Beard"

import os
import time
import math


def load_puzzle_input(file_name):
    """

    Args:
        file_name (ascii text file): puzzle input

    Returns:
    """
    with open(file_name, 'r') as file:
    return


def solve_part_1(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the sum of middle values in the correct orders in the puzzle input
    """


def solve_part_2(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the sum of middle values in the incorrect orders in the puzzle input
        once they have been re-ordered to be correct
    """


if __name__ == '__main__':
    test_input_path = os.path.dirname(__file__) + '/test_input.txt'
    input_path = os.path.dirname(__file__) + '/input.txt'

    start = time.time()
    assert solve_part_1(test_input_path) == 0
    solution_1 = solve_part_1(input_path)
    print(f"Day X part 1 solution: {solution_1}, time:{time.time()-start}")

    start = time.time()
    assert solve_part_2(test_input_path) == 0
    solution_2 = solve_part_2(input_path)
    print(f"Day X part 2 solution: {solution_2}, time:{time.time()-start}")
