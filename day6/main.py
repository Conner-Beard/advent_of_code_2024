"""
Advent of code 2024 day 5
https://adventofcode.com/2024/day/4
"""
__author__ = "Conner Beard"

import os
import time


def load_puzzle_input(file_name):
    """
    Read in the room map

    Args:
        file_name (ascii text file): puzzle input

    Returns:
        a 2d array holding the room map

    """
    array = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            array.append(list(line[:-1]))  # drop newline
    return array


directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}


def find_guard(array):
    """
    search the 2d map for the guard's posigion

    Aargs:
        array (list of lists): map of the room with guard and obsticles
    Returns:
        (row_num, col_num): position of the guard in the room
    """
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


class PositionTracker():
    """
    A class to keep track of where the guard has already been to determine if
    they are stuck in a loop, if the guard is ever in the same location facing
    the same direction then they are stuck
    """

    def __init__(self):
        self.position_history = []

    def check_stuck(self, d):
        if d in self.position_history:
            return True
        else:
            return False

    def add(self, d):
        self.position_history.append(d)

    def clear(self):
        self.position_history = []


def move_guard(array, pos):
    """
    Decide where the guard will move next and change the map to reflect that

    Args:
        array (list of lists): the room map

        pos (int, int, str): position where the guard currently is

    Returns
        array (list of lists): the updated room map

        new_pos (int, int, str): position of where the guard moved to
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
            new_pos = [pos[0], pos[1], new_move_key]
            array[new_pos[0]][new_pos[1]] = new_move_key
        else:
            new_pos = [pos[0] + move[0], pos[1] + move[1], move_key]
            array[pos[0]][pos[1]] = 'X'
            array[new_pos[0]][new_pos[1]] = move_key
    except IndexError:
        array[pos[0]][pos[1]] = 'X'
        new_pos = None

    return array, new_pos


def count_x(array):
    """
    count the number of "X" in the map, this denotes where the guard has been
    """
    x_count = 0
    for row_num, row in enumerate(array):
        for col_num, value in enumerate(row):
            if value == 'X':
                x_count = x_count + 1
    return x_count



def solve_part_1(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the number of positions that the guard visited
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
        the number of iterations where the guard got stuck
    """
    map = load_puzzle_input(file_name)

    size = 0
    for row_num, row in enumerate(map):
        for col_num, value in enumerate(map):
            size = size + 1

    stuck_counter = 0
    progress = 0
    for row_num, row in enumerate(map):
        print(progress/size)
        for col_num, value in enumerate(map):
            progress = progress + 1
            array = load_puzzle_input(file_name)

            if array[row_num][col_num] == '.':
                array[row_num][col_num] = '#'

            pos = find_guard(array)

            position_tracker = PositionTracker()

            while pos is not None:
                array, pos = move_guard(array, pos)
                if position_tracker.check_stuck(pos):
                    stuck_counter = stuck_counter + 1
                    position_tracker.clear()
                    break
                else:
                    position_tracker.add(pos)

    return stuck_counter


if __name__ == '__main__':
    test_input_path = os.path.dirname(__file__) + '/test_input.txt'
    input_path = os.path.dirname(__file__) + '/input.txt'

    start = time.time()
    assert solve_part_1(test_input_path) == 41
    solution_1 = solve_part_1(input_path)
    print(f"Day 5 part 1 solution: {solution_1}, time:{time.time()-start}")

    start = time.time()
    assert solve_part_2(test_input_path) == 6
    solution_2 = solve_part_2(input_path)
    print(f"Day 5 part 2 solution: {solution_2}, time:{time.time()-start}")
