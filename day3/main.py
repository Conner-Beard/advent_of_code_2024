"""
Advent of code 2024 day 3
https://adventofcode.com/2024/day/3
"""
__author__ = "Conner Beard"

import os
import re


def load_puzzle_input(file_name):
    """
    Read in the corrupted computer memory and extract it as a long string

    Args:
        file_name (ascii text file): puzzle input, bulk computer memory

    Returns:
        memory (string): full computer memory as a string
    """
    with open(file_name, 'r') as file:
        memory = file.read()
    return memory


def solve_part_1(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input, one report per line
        each report ints seperated by whitespace.

    Returns:
        the multiplication result of the uncorrupted computer memory sections
    """
    memory = load_puzzle_input(file_name)
    matches = re.findall('mul\((\d+,\d+)\)', memory)
    match_sum = 0
    for match in matches:
        pair = list(map(int, match.split(',')))
        mult = pair[0] * pair[1]
        match_sum = match_sum + mult
    return match_sum


def solve_part_2(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input, one report per line
        each report ints seperated by whitespace.

    Returns:
       the multiplication result of the uncorrupted computer memory sections
       wrapped by a do() and don't() clause
    """
    memory = load_puzzle_input(file_name)

    matches = re.findall("(?:(mul)\((\d+),(\d+)\))|(?:(do)\(\)|(?:(don't)\(\)))", memory)
    match_sum = 0
    mult_enabled = True
    for match in matches:
        match = list(match)
        while '' in match:
            match.remove('')

        if match[0] == 'do':
            mult_enabled = True
        elif match[0] == "don't":
            mult_enabled = False
        elif match[0] == 'mul':
            if mult_enabled:
                match_sum = match_sum + int(match[1]) * int(match[2])

    return match_sum


if __name__ == '__main__':
    test_input_path = os.path.dirname(__file__) + '/test_input.txt'
    test_input_2_path = os.path.dirname(__file__) + '/test_input_2.txt'
    input_path = os.path.dirname(__file__) + '/input.txt'

    assert solve_part_1(test_input_path) == 161
    solution_1 = solve_part_1(input_path)
    print(f"Day 3 part 1 solution: {solution_1}")

    assert solve_part_2(test_input_2_path) == 48
    solution_2 = solve_part_2(input_path)
    print(f"Day 3 part 2 solution: {solution_2}")

