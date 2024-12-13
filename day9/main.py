"""
Advent of code 2024 day X
https://adventofcode.com/2024/day/X
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
    """
    with open(file_name, 'r') as file:
        output = map(int, list(file.readlines()[0])[:-1])

    return output


def build_memory(disk_map):
    """
    Convert the disk map to a list of block id_numbers and empty space (None)
    Args:
        disk_map (list of int): a map of the memory space describing block 
        size and blank space

    Returns:
        memory (list of int and None): the expanded memory space described in
        the disk_map
    """
    id_number = 0
    block = True
    memory = []
    for info in disk_map:
        if block is True:
            memory = memory + ([id_number] * info)
            block = False
            id_number = id_number + 1
        elif block is False:
            memory = memory + ([None] * info)
            block = True
    return memory


def compress_memory(memory):
    """
    Take the memory text and shift the last element to the first space occuped
    by None until there are no None spaces left
    Args:
        memory (list of int and None): the expanded memory space described in
        the disk_map

    Returns:
        a compressed version of the memory space following the problem algo
    """
    while None in memory:
        last_value = memory.pop()
        if last_value is not None:
            for index, value in enumerate(memory):
                if value is None:
                    memory[index] = last_value
                    break
    return memory


def compress_memory_2(memory):
    """
    Take the memory text and shift the last element to the first space occuped
    by None until there are no None spaces left
    Args:
        memory (list of int and None): the expanded memory space described in
        the disk_map

    Returns:
        a compressed version of the memory space following the problem algo
    """
    current_id = max([x if x is not None else 0 for x in memory])
    while current_id > 0:
        # get positions of block at block_id 
        current_block = []
        block_size = memory.count(current_id)
        block_start = memory.index(current_id)
        for index in range(block_size):
            current_block.append(block_start + index)

        free_space = []
        for index, value in enumerate(memory):
            # print(value, current_id)
            if value == current_id:
                break

            if value is None:
                free_space.append(index)
            else:
                free_space = []
            # if enough space is found move the block
            if len(free_space) == len(current_block):
                for position in current_block:
                    memory[position] = None
                for position in free_space:
                    memory[position] = current_id
                break

        current_id = current_id - 1

    print(memory)
    return memory


def get_checksum(memory):
    """
    calculate the checksum of a compressed memory
    Args:
        memory (list of int): memory to create checksum for
    Returns:
        checksum (int): the memory checksum
    """
    checksum = 0
    for index, value in enumerate([x if x is not None else 0 for x in memory]):
        checksum = checksum + index * value
    return checksum


def solve_part_1(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the sum of middle values in the correct orders in the puzzle input
    """
    disk_map = load_puzzle_input(file_name)
    memory = build_memory(disk_map)
    compressed_memory = compress_memory(memory)
    return get_checksum(compressed_memory)


def solve_part_2(file_name):
    """
    Args:
        file_name (ascii text file): puzzle input

    Returns:
        the sum of middle values in the incorrect orders in the puzzle input
        once they have been re-ordered to be correct
    """
    disk_map = load_puzzle_input(file_name)
    memory = build_memory(disk_map)
    compressed_memory = compress_memory_2(memory)
    return get_checksum(compressed_memory)


if __name__ == '__main__':
    test_input_path = os.path.dirname(__file__) + '/test_input.txt'
    input_path = os.path.dirname(__file__) + '/input.txt'

    start = time.time()
    assert solve_part_1(test_input_path) == 1928
    solution_1 = solve_part_1(input_path)
    print(f"Day 9 part 1 solution: {solution_1}, time:{time.time()-start}")

    start = time.time()
    assert solve_part_2(test_input_path) == 2858
    solution_2 = solve_part_2(input_path)
    print(f"Day 9 part 2 solution: {solution_2}, time:{time.time()-start}")
