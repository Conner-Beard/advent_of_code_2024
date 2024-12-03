"""
Advent of code 2024 day 2
https://adventofcode.com/2024/day/2
"""
__author__ = "Conner Beard"

import os


def load_reactor_reports(file_name):
    """
    Read in the puzzle input file and extract the reactor reports

    Args:
        file_name (ascii text file): puzzle input, one report per line
        each report ints seperated by whitespace.

    Returns:
        report_list (list of lists of int): reactor reports
    """
    report_list = []
    with open(file_name, 'r') as file:
        for report in [x.split() for x in file.readlines()]:
            report_list.append([int(x) for x in report])
    return report_list


def test_monotonic(series, max_slope=3, tolerance=0):
    """
    Tests if a serise of numbers always increases/decreases

    Args:
        series (list of int): a list of numbers to test

        max_slope (int): the maximum difference allowed between adjacent
        elements

        tolerance (int): the number of check failures allowed before the series
        is makred as unsafe

    Returns:
        result (bool): returns true if the series is safe
    """
    if abs(series[0] - series[1]) > max_slope:
        series = series[1:]
        tolerance = tolerance - 1
        if tolerance < 0:
            return False

    previous_value = series[0]
    previous_gradiant = None
    for value in series[1:]:
        pop_value = False
        slope = value - previous_value

        if abs(slope) > max_slope:
            pop_value = True

        if value > previous_value:
            gradiant = 1
        elif value < previous_value:
            gradiant = -1
        else:
            gradiant = 0
            pop_value = True

        if (gradiant != previous_gradiant) and (previous_gradiant is not None):
            pop_value = True

        if pop_value and (tolerance != 0):
            tolerance = tolerance - 1
            previous_value = previous_value
            previous_gradiant = previous_gradiant
            continue
        elif pop_value and (tolerance == 0):
            return False
        elif pop_value is False:
            previous_value = value
            previous_gradiant = gradiant
        else:
            raise Exception('Invalid case!')

    return True


def solve_part_1(file_name):
    """
    Determine how many given reactor reports are safe

    a report is safe if list elements are monotonic

    AND

    adjacent list elements differ by at least 1 and at most 3

    Args:
        file_name (ascii text file): puzzle input, one report per line
        each report ints seperated by whitespace.

    Returns:
        the number of safe reactor reports
    """
    report_list = load_reactor_reports(file_name)
    safe_reports = []
    for report in report_list:
        if test_monotonic(report) is True:
            safe_reports.append(report)
    return len(safe_reports)


def solve_part_2(file_name):
    """
    like part 1 except we can ignore one failure

    Args:
        file_name (ascii text file): puzzle input, one report per line
        each report ints seperated by whitespace.

    Returns:
        the number of safe reactor reports while ignoring one failing element
    """
    report_list = load_reactor_reports(file_name)
    safe_reports = []
    for report in report_list:
        if test_monotonic(report) is True:
            safe_reports.append(report)
        else:
            for index, value in enumerate(report):
                subset = report[0:index] + report[index+1:]
                if test_monotonic(subset) is True:
                    safe_reports.append(subset)
                    break
    return len(safe_reports)


if __name__ == '__main__':
    test_input_path = os.path.dirname(__file__) + '/test_input.txt'
    input_path = os.path.dirname(__file__) + '/input.txt'

    assert solve_part_1(test_input_path) == 2
    solution_1 = solve_part_1(input_path)
    print(f"Day 1 part 1 solution: {solution_1}")

    assert solve_part_2(test_input_path) == 8
    solution_2 = solve_part_2(input_path)
    print(f"Day 1 part 2 solution: {solution_2}")
