"""
Advent of code 2024 day 10
https://adventofcode.com/2024/day/10
"""
__author__ = "Conner Beard"

import os
import time


def load_puzzle_input(file_name):
    """

    Args:
        file_name (ascii text file): puzzle input

    Returns:
        puzzle input
    """
    array = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            row = []
            for value in line[:-1]:
                row.append(int(value))
            array.append(row)
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


def follow_trail(start_row, start_col, array, depth=0):
    """
    Recursive function to follow trails to their endponints and add each
    unique endpoint to a set.
    Args:
        start_row (int): array row of current trail tile

        start_col (int): array col of current trail tile

        array (list of list of int): map representation

        depth (int): recursion depth
    Returns:
        a set of valid trail endpoints for the top level recursion call
    """
    if depth > 11:
        raise RecursionError('Trail overflow')

    assert array[start_row][start_col] != 9

    directions = {'up': (start_row - 1, start_col),
                  'down': (start_row + 1, start_col),
                  'left': (start_row, start_col - 1),
                  'right': (start_row, start_col + 1)}

    found_ends = set()
    found_paths = 0
    for row, col in directions.values():
        if check_bounds(row, col, array) is False:
            continue
        if (array[row][col] == 9) & (array[start_row][start_col] == 8):
            found_ends.add((row, col))
            found_paths = found_paths + 1
        elif array[row][col] == array[start_row][start_col] + 1:
            ends, paths = follow_trail(row, col, array, depth + 1)
            found_ends = found_ends.union(ends)
            found_paths = found_paths + paths
    return found_ends, found_paths


def solve_part_1(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the number of unique endpoints reachable from trailheads
    """
    array = load_puzzle_input(file_name)
    total_score = 0
    for row_num, row in enumerate(array):
        for col_num, value in enumerate(row):
            if value == 0:
                ends, paths = follow_trail(row_num, col_num, array)
                score = len(ends)
                total_score = total_score + score
    return total_score


def solve_part_2(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the number of unique paths to endpoints reachable from trailheads
    """
    array = load_puzzle_input(file_name)
    total_score = 0
    for row_num, row in enumerate(array):
        for col_num, value in enumerate(row):
            if value == 0:
                ends, paths = follow_trail(row_num, col_num, array)
                score = paths
                total_score = total_score + score
    return total_score


if __name__ == '__main__':
    test_input_path = os.path.dirname(__file__) + '/test_input.txt'
    input_path = os.path.dirname(__file__) + '/input.txt'

    start = time.time()
    assert solve_part_1(test_input_path) == 36
    solution_1 = solve_part_1(input_path)
    print(f"Day 10 part 1 solution: {solution_1}, time:{time.time()-start}")

    start = time.time()
    assert solve_part_2(test_input_path) == 81
    solution_2 = solve_part_2(input_path)
    print(f"Day 10 part 2 solution: {solution_2}, time:{time.time()-start}")
