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
