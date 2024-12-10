"""
Advent of code 2024 day 5
https://adventofcode.com/2024/day/4
"""
__author__ = "Conner Beard"

import os
import time

def load_puzzle_input(file_name):
    """
    Read in the crossword puzzle

    Args:
        file_name (ascii text file): puzzle input

    Returns:

    """
    array = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            array.append(list(line[:-1]))  # drop newline
    return array


directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}


def find_guard(array):
    for row_num, row in enumerate(array):
        for col_num, value in enumerate(row):
            if value in directions.keys():
                return [row_num, col_num]

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


def move_guard(array, pos):
    """
    Decide where the guard will move next

    Args:
        array ():

        pos ():
    """
    move_key = array[pos[0]][pos[1]]
    move = directions[move_key]

    new_move_key = list(directions.keys())[(list(directions.keys()).index(move_key)+1) % 4]

    try:
        if (pos[0] + move[0]) < 0:
            raise IndexError
        if (pos[1] + move[1]) < 0:
            raise IndexError
        if array[pos[0] + move[0]][pos[1] + move[1]] == '#':
            new_pos = [pos[0], pos[1]]
            array[new_pos[0]][new_pos[1]] = new_move_key
        else:
            new_pos = [pos[0] + move[0], pos[1] + move[1]]
            array[pos[0]][pos[1]] = 'X'
            array[new_pos[0]][new_pos[1]] = move_key
    except IndexError:
        array[pos[0]][pos[1]] = 'X'
        new_pos = None

    return array, new_pos


def count_x(array):
    x_count = 0
    for row_num, row in enumerate(array):
        for col_num, value in enumerate(row):
            if value == 'X':
                x_count = x_count + 1
    return x_count


def print_array(array):
    string = ''
    for row in array:
        string = string + ''.join(row) + '\n'
    print(string)
    with open('temp.txt', 'w') as file:
        file.write(string)


def solve_part_1(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
    """
    array = load_puzzle_input(file_name)

    pos = find_guard(array)

    while pos is not None:
        array, pos = move_guard(array, pos)

    return count_x(array)


def solve_part_2(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
    """


if __name__ == '__main__':
    test_input_path = os.path.dirname(__file__) + '/test_input.txt'
    input_path = os.path.dirname(__file__) + '/input.txt'

    start = time.time()
    assert solve_part_1(test_input_path) == 41
    solution_1 = solve_part_1(input_path)
    print(f"Day 5 part 1 solution: {solution_1}, time:{time.time()-start}")

    start = time.time()
    assert solve_part_2(test_input_path) == 123
    solution_2 = solve_part_2(input_path)
    print(f"Day 5 part 2 solution: {solution_2}, time:{time.time()-start}")
