"""
Advent of code 2024 day 11
https://adventofcode.com/2024/day/11
"""
__author__ = "Conner Beard"

import os
import time
from functools import cache


def load_puzzle_input(file_name):
    """

    Args:
        file_name (ascii text file): puzzle input

    Returns:
        stones (list): stones that appear in the room
    """
    with open(file_name, 'r') as file:
        stones = list(map(int, file.readlines()[0].split()))
    return stones


@cache
def get_stone(stone):
    """
    determine the next stones that will appear when a stone is blinked at
    Args:
        stone (int): the stone being observed

    Returns:
        (tuple): the stone(s) that appear after blinking
    """
    if (len(str(stone)) % 2 == 0):
        middle = len(str(stone))//2
        return tuple([int(str(stone)[0:middle]), int(str(stone)[middle:])])
    elif stone == 0:
        return tuple([1])
    else:
        return tuple([int(stone * 2024)])


@cache  # memoization to shortcut previously seen stone/blink/depth combos
def recursive_blink(stone, blinks, depth=0):
    """
    Recursive function that counts the number of final stones after X blinks
    uses memoization to avoid calling recursively for previously seen stones
    Args:
        stone (int): the number of the stone being watched

        blinks (int): number of blinks given to the stone to reach its final
        state

        depth (int): recursion depth tracker
    """
    count = 0
    depth = depth + 1
    if depth > blinks:
        return 1  # reached a final stone
    elif depth > 100:
        raise Exception("Hit recursion limit")

    stones = get_stone(stone)

    for new_stone in stones:
        count = count + recursive_blink(new_stone, blinks, depth)

    return count


def solve_part_1(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        The number of stones in the room after 25 blinks

    """
    start_stones = load_puzzle_input(file_name)
    final_count = 0
    for stone in start_stones:
        count = recursive_blink(stone, 25)
        final_count = final_count + count

    print(final_count)
    return final_count


def solve_part_2(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        The number of stones in the room after 75 blinks

    """
    start_stones = load_puzzle_input(file_name)
    final_count = 0
    for stone in start_stones:
        count = recursive_blink(stone, 75)
        final_count = final_count + count

    print(final_count)
    return final_count


if __name__ == '__main__':
    test_input_path = os.path.dirname(__file__) + '/test_input.txt'
    input_path = os.path.dirname(__file__) + '/input.txt'

    start = time.time()
    assert solve_part_1(test_input_path) == 55312
    solution_1 = solve_part_1(input_path)
    print(f"Day 11 part 1 solution: {solution_1}, time:{time.time()-start}")

    solution_2 = solve_part_2(input_path)
    print(f"Day 11 part 2 solution: {solution_2}, time:{time.time()-start}")
