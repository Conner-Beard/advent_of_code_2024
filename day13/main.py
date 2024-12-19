"""
Advent of code 2024 day 13
https://adventofcode.com/2024/day/13
"""
__author__ = "Conner Beard"

import os
import time
from decimal import Decimal, getcontext


def load_puzzle_input(file_name, offset=0):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        load the machine controls
    """
    machines = []
    machine = {}
    with open(file_name, 'r') as file:
        for line in file.readlines():
            if ("Button A" in line) or ("Button B" in line):
                for char in 'XY,:':
                    line = line.replace(char, '')
                line = line.split()
                button = line[1].lower()
                x = int(line[2])
                y = int(line[3])
                machine[button] = (x, y)
            elif "Prize" in line:
                for char in 'XY=,':
                    line = line.replace(char, '')
                line = line.split()
                x = int(line[1])+offset
                y = int(line[2])+offset
                machine['prize'] = (x, y)
                machines.append(machine)
                machine = {}
    return machines


def add_coordinates(pair1, pair2):
    """
    add two coordinates together
    Args:
        pair1 (int, int): first coordinate

        pair2 (int, int): second coordinate
    Return:
        (int, int): new coordinate
    """
    return (pair1[0]+pair2[0], pair1[1]+pair2[1])


def multipy_coordinate(pair, mult):
    """
    add two coordinates together
    Args:
        pair1 (int, int): coordinate

        mult (int): scalar value
    Return:
        (int, int): new coordinate after multiplication
    """
    return (int(pair[0] * mult), int(pair[1] * mult))


def equate_coordinates(pair1, pair2):
    """
    add two coordinates together
    Args:
        pair1 (int, int): first coordinate

        pair2 (int, int): second coordinate
    Return:
        (True/False): True if coordinates are equal
    """
    if (pair1[0] == pair2[0]) and (pair1[1] == pair2[1]):
        return True
    else:
        return False


def solve(x1, y1, x2, y2, x3, y3):
    """
    Determine how (x1, y1) and (x2, y2) can be multiplied and summed to reach
    (x3, y3)
    Args:
        x1 (int)

        y1 (int)

        x2 (int)

        y2 (int)

        x3 (int)

        y3 (int)

    Return:
        price (int): the price of reaching (x3, y3) or 0 if unreachable
    """
    getcontext().prec = 1000
    x1 = Decimal(x1)
    y1 = Decimal(y1)
    x2 = Decimal(x2)
    y2 = Decimal(y2)
    x3 = Decimal(x3)
    y3 = Decimal(y3)

    a = (x3 - ((y3 * x2) / y2)) / (x1 - ((y1 * x2) / y2))
    b = (x3 - a*x1) / x2

    # decimal is still producing numbers with precision errors, round out to
    # 500 digits
    a = round(a, 500)
    b = round(b, 500)

    price = int(a*3 + b*1)

    if (a.as_integer_ratio()[1] == 1) & (b.as_integer_ratio()[1] == 1):
        return price
    else:
        return 0


def solve_part_1(file_name, mode='smart'):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the price of reaching all the prizes
    """
    machines = load_puzzle_input(file_name)

    total = 0
    for machine in machines:
        if mode == 'brute':
            solutions = []
            for a_presses in range(1, 101):
                for b_presses in range(1, 101):
                    pos_a = multipy_coordinate(machine['a'], a_presses)
                    pos_b = multipy_coordinate(machine['b'], b_presses)
                    grabber_pos = add_coordinates(pos_a, pos_b)
                    if equate_coordinates(grabber_pos, machine['prize']):
                        solutions.append((a_presses * 3) + (b_presses * 1))

            if len(solutions) > 0:
                price = min(solutions)
            else:
                price = 0
        elif mode == 'smart':
            price = solve(machine['a'][0], machine['a'][1],
                          machine['b'][0], machine['b'][1],
                          machine['prize'][0], machine['prize'][1])

        total = total + price
    return total


def solve_part_2(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the price of reaching all the prizes without the unforunate conversion
        error
    """
    machines = load_puzzle_input(file_name, offset=10000000000000)

    total = 0
    for machine in machines:
        price = solve(machine['a'][0], machine['a'][1],
                      machine['b'][0], machine['b'][1],
                      machine['prize'][0], machine['prize'][1])
        total = total + price

    return total



if __name__ == '__main__':
    test_input_path = os.path.dirname(__file__) + '/test_input.txt'
    input_path = os.path.dirname(__file__) + '/input.txt'

    start = time.time()
    assert solve_part_1(test_input_path) == 480
    solution_1 = solve_part_1(input_path)
    assert solution_1 == 31589
    print(f"Day 13 part 1 solution: {solution_1}, time:{time.time()-start}")

    start = time.time()
    # assert solve_part_2(test_input_path) == 0
    solution_2 = solve_part_2(input_path)
    print(f"Day 13 part 2 solution: {solution_2}, time:{time.time()-start}")
