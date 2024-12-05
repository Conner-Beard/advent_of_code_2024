"""
Advent of code 2024 day 5
https://adventofcode.com/2024/day/4
"""
__author__ = "Conner Beard"

import os
import time
import math


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
    rules = []
    orders = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            if '|' in line:
                rule = list(map(int, line.strip('\n').split('|')))
                rules.append(rule)
            elif ',' in line:
                order = list(map(int, line.strip('\n').split(',')))
                orders.append(order)
    return rules, orders


def is_order_good(rules, order):
    """
    Test if any of the order element ordering violates the rules in rules
    Args:
        rules (list of list of two int): each element describes an ordering
        rule for order

        order (list of int): a list of values that may or may not follow the
        ordering in rules
    returns:
        (True or rule_pair): if the order is good return True, otherwise
        return the first rule causing a failiure
    """
    for rule in rules:
        found_order = []
        for value in order:
            if value == rule[0]:
                found_order.append(0)
            if value == rule[1]:
                found_order.append(1)
        if found_order == [1, 0]:
            return rule
    else:
        return True


def solve_part_1(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the sum of middle values in the correct orders in the puzzle input
    """
    rules, orders = load_puzzle_input(file_name)
    good_orders = []
    for order in orders:
        if is_order_good(rules, order) is True:
            good_orders.append(order[math.floor(len(order)/2)])

    return sum(good_orders)


def solve_part_2(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the sum of middle values in the incorrect orders in the puzzle input
        once they have been re-ordered to be correct
    """
    rules, orders = load_puzzle_input(file_name)
    bad_orders = []
    for order in orders:
        if is_order_good(rules, order) is not True:
            bad_orders.append(order)

    fixed_orders = []
    for order in bad_orders:
        fixed_order = order
        while True:
            result = is_order_good(rules, fixed_order)
            if result is True:
                fixed_orders.append(fixed_order[math.floor(len(fixed_order)/2)])
                break
            else:
                pos_1 = fixed_order.index(result[0])
                pos_2 = fixed_order.index(result[1])
                fixed_order[pos_1] = result[1]
                fixed_order[pos_2] = result[0]

    return sum(fixed_orders)


if __name__ == '__main__':
    test_input_path = os.path.dirname(__file__) + '/test_input.txt'
    input_path = os.path.dirname(__file__) + '/input.txt'

    start = time.time()
    assert solve_part_1(test_input_path) == 143
    solution_1 = solve_part_1(input_path)
    print(f"Day 5 part 1 solution: {solution_1}, time:{time.time()-start}")

    start = time.time()
    assert solve_part_2(test_input_path) == 123
    solution_2 = solve_part_2(input_path)
    print(f"Day 5 part 2 solution: {solution_2}, time:{time.time()-start}")
