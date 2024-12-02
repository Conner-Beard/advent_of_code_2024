"""
Advent of code 2024 day 1
https://adventofcode.com/2024/day/1
"""
__author__ = "Conner Beard"


def get_location_lists(file_name):
    """
    Read in the puzzle input file and extract the two location ID lists.

    Args:
        file_name (ascii text file): puzzle input, two numbers per line
        seperated by whitespace.

    Returns:
        list_a (list of int): first location list
        list_b (list of int): second location list
    """
    list_a = []
    list_b = []
    with open(file_name, 'r') as file:
        for element1, element2 in [x.split() for x in file.readlines()]:
            list_a.append(int(element1))
            list_b.append(int(element2))
    return list_a, list_b


def get_distance(list_a, list_b):
    """
    For two lists of the same length, get the numerical distance between each
    element at the same index.

    Args:
        list_a (list of int): first location list
        list_b (list of int): second location list

    Returns:
        total_distance: summation of numerical distance between list elements
    """
    assert len(list_a) == len(list_b)

    distances = []
    for index, value in enumerate(list_a):
        distance = abs(list_a[index] - list_b[index])
        distances.append(distance)

    total_distance = sum(distances)

    return total_distance


def get_similarity(list_a, list_b):
    """
    Get a similarity score based on the number of occurances of elements
    in list_a in list_b, multiplied by the element value.

    Args:
        list_a (list of int): first location list
        list_b (list of int): second location list

    Returns:
        total_similarity: similarity score between list_a and list_b
    """
    assert len(list_a) == len(list_b)

    similarities = []
    for value in list_a:
        count = list_b.count(value)
        similarity = value * count
        similarities.append(similarity)

    total_similarity = sum(similarities)

    return total_similarity


def solve_part_1(file_name):
    """
    Get the total "distance" between the two lists from day 1.

    Args:
        file_name (ascii text file): puzzle input, two numbers per line
        seperated by whitespace.

    Returns:
        total_distance: summation of numerical distance between list elements
    """
    list_a, list_b = get_location_lists(file_name)
    for location_list in [list_a, list_b]:
        location_list.sort()
    total_distance = get_distance(list_a, list_b)

    return total_distance


def solve_part_2(file_name):
    """
    Get the total "similarity" between the two lists from day 1.

    Args:
        file_name (ascii text file): puzzle input, two numbers per line
        seperated by whitespace.

    Returns:
        total_similarity: similarity score between list_a and list_b
    """
    list_a, list_b = get_location_lists(file_name)
    total_similarity = get_similarity(list_a, list_b)

    return total_similarity


if __name__ == '__main__':
    assert solve_part_1('test_input.txt') == 11
    total_distance = solve_part_1('input.txt')
    print(f"Part 1 solution: {total_distance}")

    assert solve_part_2('test_input.txt') == 31
    total_similarity = solve_part_2('input.txt')
    print(f"Part 2 solution: {total_similarity}")
