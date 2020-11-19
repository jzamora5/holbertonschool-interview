#!/usr/bin/python3
"""
Module for Rain Task
"""


def check_ahead(walls, a, j):
    """ Checks if there are greater or equal values ahead """
    check = False
    middle = []

    while j < len(walls):
        if a < walls[j] or a == walls[j]:
            check = True
            break
        middle.append(walls[j])
        j += 1

    return check, middle, j


def rain(walls):
    """
    Given a list of non-negative integers representing walls of width 1,
    calculate how much water will be retained after it rains.

    - Prototype: def rain(walls)
    - walls is a list of non-negative integers.
    - Return: Integer indicating total amount of rainwater retained.
    - Assume that the ends of the list
    (before index 0 and after index walls[-1])
    are not walls, meaning they will not retain water.
    - If the list is empty return 0.
    """
    if not walls or not isinstance(walls, list):
        return 0

    i, water, middle, no_start = 0, 0, [], 0
    a, b, idx_a, idx_b = 0, 0, 0, 0

    while i < len(walls):

        if walls[i] == 0:
            if no_start:
                middle.append(0)
            i += 1
            continue

        no_start = 1

        if not a:
            a = walls[i]
            idx_a = i
        else:
            b = walls[i]
            idx_b = i

        if not a or not b:
            i += 1
            continue

        if a < b:
            water += a * len(middle)

        else:
            check, sub_middle, j = check_ahead(walls, a, idx_a + 1)

            if not check:
                water += b * len(middle)
            else:
                i, middle = j, sub_middle
                b, idx_b = walls[i], i

                c = a if a < walls[i] else walls[i]
                water += c * len(middle) - sum(middle)

        middle = []
        i += 1
        a, b, idx_a, idx_b = b, 0, idx_b, 0

    return water
