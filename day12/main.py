"""
Advent of code 2024 day 12
https://adventofcode.com/2024/day/12
"""
__author__ = "Conner Beard"

import os
import time


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
    """
    Hunts down connecting farm tiles and returns a set of all the tiles within
    one farm plot of the same crop type.
    Args:
        farm (2d array): a map of the farm crops on a 2d gird

        crop (str): the letter representation of the crop

        row_num (int): the row of the current tile

        col_num (int): the col of the current tile

        inside_plot (set of coordinates): all of the tiles farm tiles currently
        identified as inside the current plot

        depth (int): the recursion depth
    Returns:
        inside_plot(set of coordinates): all the farm tiles with the plot of
        crop type
    """
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
    """
    gets the perimeter value of the plot
    Args:
        plot (set of coordinates): set of adjacent tiles that make up the plot
    Returns:
        preimeter (int): the perimeter of the shape made by the plot
    """
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


def group_by_consecutive(values):
    """
    takes a list and converts it to a list of consecutive values in the input
    list

    Args:
        values (list of int): values to be sorted
    Returns:
        (list of list): the input values sorded into consecutive ordered lists
    """
    if len(values) == 0:
        return []

    values.sort()
    output = []

    previous_value = values[0]

    group = [values[0]]
    for value in values[1:]:
        if value == previous_value + 1:
            group.append(value)
        else:
            output.append(group)
            group = []
            group.append(value)
        previous_value = value

    if group != group[-1]:
        output.append(group)

    return output


def get_slice_sides(checked, plot, orientation='row'):
    """
    takes a dictinary of vertical or horizontal slices of the plot and counts
    the consecutive sides that are exposed to other crops
    Args:
        checked (dict of list of int): slices of the plot

        plot (set of coordinates): set of adjacent tiles that make up the plot

        orientation ('row' or 'col'): the orientation of the checked values
    Returns:
        sides (int): the sides of the checked value that are exposed to other
        crops
    """
    side_count = 0
    if orientation == 'row':
        for row, col_list in checked.items():
            for group in group_by_consecutive(col_list):
                top_side = []
                bot_side = []
                for col in group:
                    if (row-1, col) not in plot:
                        top_side.append(col)
                    if (row+1, col) not in plot:
                        bot_side.append(col)
                top_count = len(group_by_consecutive(top_side))
                bot_count = len(group_by_consecutive(bot_side))
                side_count = side_count + top_count + bot_count
    elif orientation == 'col':
        for col, row_list in checked.items():
            for group in group_by_consecutive(row_list):
                left_side = []
                right_side = []
                for row in group:
                    if (row, col-1) not in plot:
                        left_side.append(row)
                    if (row, col+1) not in plot:
                        right_side.append(row)
                left_count = len(group_by_consecutive(left_side))
                right_count = len(group_by_consecutive(right_side))
                side_count = side_count + right_count + left_count
    return side_count


def get_sides(plot):
    """
    counts the sides of a plot that are touching other crops
    Args:
        plot (set of coordinates): set of adjacent tiles that make up the plot
    Returns:
        sides (int): the sides that are exposed to other crops
    """
    checked_row = {}
    checked_col = {}
    for row, col in plot:
        checked_row[row] = []
        checked_col[col] = []
        for other_row, other_col in plot:
            if row == other_row:
                checked_row[row].append(other_col)
            if col == other_col:
                checked_col[col].append(other_row)

    total_sides = 0
    vertical_sides = get_slice_sides(checked_row, plot, orientation='row')
    horizontal_sides = get_slice_sides(checked_col, plot, orientation='col')
    total_sides = vertical_sides + horizontal_sides

    return total_sides


def solve_part_1(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        price of a fencing the farm without discount
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
        price of a fencing the farm with discount
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
    print(f"Day 12 part 1 solution: {solution_1}, time:{time.time()-start}")

    start = time.time()
    assert solve_part_2(test_input_path) == 1206
    solution_2 = solve_part_2(input_path)
    print(f"Day 12 part 2 solution: {solution_2}, time:{time.time()-start}")
