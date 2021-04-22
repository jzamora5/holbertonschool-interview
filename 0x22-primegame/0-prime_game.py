#!/usr/bin/python3

""" Prime Game Algorithm Python """


def is_prime(n):
    """ Checks if a number is a primer number """

    if n <= 1:
        return False

    flag = False
    for i in range(2, n):
        if (n % i) == 0:
            flag = True
            break

    return False if flag else True


def num_of_multiples_in_list(n, arr):
    """ Counts how many multiples of n are in arr """
    count = 0
    for num in arr:
        if num % n == 0:
            count += 1

    return count


def best_num_option(arr):
    """ Finds the best number to pick in prime game """

    best_option = {"value": None, "multiples": 0}

    for option in arr:
        if not is_prime(option):
            continue

        n_multiples = num_of_multiples_in_list(option, arr)
        if n_multiples > best_option["multiples"]:
            best_option["value"] = option
            best_option["multiples"] = n_multiples

    return best_option["value"]


def remove_multiples(n, arr):
    """ Removes multiples of n from arr """
    temp_list = arr[:]
    for num in temp_list:
        if not num % n:
            arr.remove(num)


def isWinner(x, nums):
    """
    x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """

    players_wins = {"Maria": 0, "Ben": 0}

    for round in range(x):
        round_nums = [i for i in range(1, nums[round] + 1)]
        best_play, player = best_num_option(round_nums), "Maria"
        turn = 0

        while(best_play):
            player = "Maria" if not turn % 2 else "Ben"

            best_play = best_num_option(round_nums)
            if not best_play:
                break

            remove_multiples(best_play, round_nums)
            turn += 1

        if player == "Maria":
            players_wins["Ben"] += 1
        else:
            players_wins["Maria"] += 1

    if players_wins["Maria"] > players_wins["Ben"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"

    return None
