#!/usr/bin/python3
"""Module of the primeGame"""


def isWinner(x, nums):
    """returns the name of winner"""
    if not nums or x < 1:
        return None
    if x > 10000:
        return None
    b = 0
    m = 0

    players = ["Maria", "Ben"]
    for i in range(len(nums)):
        if nums[i] > 10000:
            return None
        if nums[i] == 1:
            b += 1
        elif nums[i] % 2 == 0:
            b += 1
        else:
            m += 1
    if b > m:
        return players[1]
    if b == m:
        return None
    return players[0]
