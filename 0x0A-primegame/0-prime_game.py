#!/usr/bin/python3
"""Module of the primeGame"""


def isWinner(x, nums):
    """returns the name of winner"""
    if not nums or x < 1:
        return None

    players = ["Maria", "Ben"]
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            return players[1]
        return players[0]
