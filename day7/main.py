"""
Advent of code 2024 day 7
https://adventofcode.com/2024/day/7
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
        equations (list of lists): list of equations with answer operand pairs
    """
    equations = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            result, operands = line.split(':')
            result = int(result)
            operands = operands.split()
            operands = list(map(int, operands))
            equations.append((result, operands))
    return equations


def get_answers(equation):
    """
    get all the possible answers to the provided equation operands given the
    + and * operators
    Args:
        equation (answer, operands(list)): eqatiion to get answers for
    Returs:
        all the possible solutions given the equation operands and the
        operators
    """
    solutions = [equation[1][0]]
    for operand in equation[1][1:]:
        working_solutions = []
        for solution in solutions:
            mult = solution * operand
            add = solution + operand

            working_solutions.append(mult)
            working_solutions.append(add)
        solutions = working_solutions
    return solutions


def get_answers_with_concat(equation):
    """
    get all the possible answers to the provided equation operands given the
    +, *, and || operators
    Args:
        equation (answer, operands(list)): eqatiion to get answers for
    Returs:
        all the possible solutions given the equation operands and the
        operators
    """
    solutions = [equation[1][0]]
    for operand in equation[1][1:]:
        working_solutions = []
        for solution in solutions:
            mult = solution * operand
            add = solution + operand
            concat = int(str(solution) + str(operand))

            working_solutions.append(mult)
            working_solutions.append(add)
            working_solutions.append(concat)
        solutions = working_solutions
    return solutions


def solve_part_1(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the sum of middle values in the correct orders in the puzzle input
    """
    equations = load_puzzle_input(file_name)

    solvable = []
    for equation in equations:
        answers = get_answers(equation)
        if equation[0] in answers:
            solvable.append(equation[0])

    return sum(solvable)


def solve_part_2(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the sum of middle values in the incorrect orders in the puzzle input
        once they have been re-ordered to be correct
    """
    equations = load_puzzle_input(file_name)

    solvable = []
    for equation in equations:
        answers = get_answers_with_concat(equation)
        if equation[0] in answers:
            solvable.append(equation[0])

    return sum(solvable)


if __name__ == '__main__':
    test_input_path = os.path.dirname(__file__) + '/test_input.txt'
    input_path = os.path.dirname(__file__) + '/input.txt'

    start = time.time()
    assert solve_part_1(test_input_path) == 3749
    solution_1 = solve_part_1(input_path)
    print(f"Day 7 part 1 solution: {solution_1}, time:{time.time()-start}")

    start = time.time()
    assert solve_part_2(test_input_path) == 11387
    solution_2 = solve_part_2(input_path)
    print(f"Day 7 part 2 solution: {solution_2}, time:{time.time()-start}")
