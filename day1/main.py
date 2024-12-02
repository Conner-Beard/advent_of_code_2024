"""
Advent of code 2024 day 1
https://adventofcode.com/2024/day/1
"""
__author__ = "Conner Beard"


def get_location_lists(file_name):
    """
    Read in the puzzle input file and extract the two location ID lists.
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
    """
    assert len(list_a) == len(list_b)

    distances = []
    for index, value in enumerate(list_a):
        distance = abs(list_a[index] - list_b[index])
        distances.append(distance)

    return distances


def get_similarity(list_a, list_b):
    """
    Get a similarity score based on the number of occurances of elements
    in list_a in list_b, multiplied by the element value.
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
    """
    list_a, list_b = get_location_lists(file_name)
    for location_list in [list_a, list_b]:
        location_list.sort()
    distances = get_distance(list_a, list_b)
    total_distance = sum(distances)

    return total_distance


def solve_part_2(file_name):
    """
    Get the total "similarity" between the two lists from day 1.
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
