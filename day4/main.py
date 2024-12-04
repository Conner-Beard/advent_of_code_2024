"""
Advent of code 2024 day 4
https://adventofcode.com/2024/day/4
"""
__author__ = "Conner Beard"

import os
from itertools import product


def load_puzzle_input(file_name):
    """
    Read in the crossword puzzle

    Args:
        file_name (ascii text file): puzzle input

    Returns:
        array (2d array): crossword as 2d array
    """
    array = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            array.append(list(line[:-1]))  # drop newline
    return array


def index_array(array, row, col):
    """
    Index a 2d array while disallowing negative index

    Args:
        array (2d array)

        row (int)

        col (int)

    Returns:
        value at array(row, col)
    """
    if (row < 0) or (col < 0):
        raise IndexError
    return array[row][col]


def look_for_pattern(array, row_num, col_num, target_pattern):
    """
    Searches for target_pattern in an array of values, will match target
    pattern in any direction (forward, backward, diagonal, up, down)
    Args:
        array (2d array): 2d array of values to search in

        row_num (int): row number to start search in

        col_num (int): col number to start search in

        target_pattern (list of str): list of single values to search
        for in order
    Return:
        number of matches starting at array(row_num, col_num)
    """
    search_directions = list(product([-1, 0, 1], [-1, 0, 1]))
    search_directions.remove((0, 0))
    matches = []
    for row_dir, col_dir in search_directions:
        possible_match = []
        for index, pattern in enumerate(target_pattern):
            row_off = row_dir*(index)
            col_off = col_dir*(index)
            possible_match.append((row_num + row_off, col_num + col_off))
            try:
                adjacent_value = index_array(array,
                                             row_num + row_off,
                                             col_num + col_off)
            except IndexError:
                break
            if adjacent_value != pattern:
                break
        else:
            matches.append(possible_match)
    return matches


def look_for_diagonal_pattern(array, row_num, col_num, target_pattern):
    """
    Searches for target_pattern in an array of values, will match target
    pattern in only diagonal directions
    Args:
        array (2d array): 2d array of values to search in

        row_num (int): row number to start search in

        col_num (int): col number to start search in

        target_pattern (list of str): list of single values to search
        for in order
    Return:
        number of matches starting at array(row_num, col_num)
    """
    search_directions = list(product([-1, 1], [-1, 1]))
    matches = []
    for row_dir, col_dir in search_directions:
        possible_match = []
        for index, pattern in enumerate(target_pattern):
            row_off = row_dir*(index)
            col_off = col_dir*(index)
            possible_match.append((row_num + row_off, col_num + col_off))
            try:
                adjacent_value = index_array(array,
                                             row_num + row_off,
                                             col_num + col_off)
            except IndexError:
                break
            if adjacent_value != pattern:
                break
        else:
            matches.append(possible_match)
    return matches


def solve_part_1(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the count of 'XMAS' in puzzle
    """
    array = load_puzzle_input(file_name)
    matches = []
    target_pattern = ['X', 'M', 'A', 'S']
    for row_number, row in enumerate(array):
        for column_number, value in enumerate(row):
            matches = matches + look_for_pattern(array,
                                                 row_number,
                                                 column_number,
                                                 target_pattern)
    return len(matches)


def solve_part_2(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the count of 'MAS' in the shape of an X in the puzzle
    """
    array = load_puzzle_input(file_name)
    matches = []
    target_pattern = ['M', 'A', 'S']
    for row_number, row in enumerate(array):
        for column_number, value in enumerate(row):
            matches = matches + look_for_diagonal_pattern(array,
                                                          row_number,
                                                          column_number,
                                                          target_pattern)

    # position 2 will always be an 'A', match is only valid if position
    # 2 appears twice in the full list of matches
    xmas_positions = []
    for index, match in enumerate(matches):
        for match_comp in matches[0:index] + matches[index+1:]:
            if match_comp[1] == match[1]:
                xmas_positions.append(match[1])
    # reduce duplicate matches by converting to set
    return len(set(xmas_positions))


if __name__ == '__main__':
    test_input_path = os.path.dirname(__file__) + '/test_input.txt'
    input_path = os.path.dirname(__file__) + '/input.txt'

    assert solve_part_1(test_input_path) == 18
    solution_1 = solve_part_1(input_path)
    print(f"Day 4 part 1 solution: {solution_1}")

    assert solve_part_2(test_input_path) == 9
    solution_2 = solve_part_2(input_path)
    print(f"Day 4 part 2 solution: {solution_2}")
