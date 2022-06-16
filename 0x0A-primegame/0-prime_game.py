#!/usr/bin/python3
"""Program that performs prime game"""


def isWinner(x, nums):
    """Function that performs prime game"""
    if not nums or x < 1:
        return None
    players = ['Maria', 'Ben']
    n = max(nums)
    fltr = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not fltr[i]:
            continue
        for j in range(i * i, n + 1, i):
            fltr[j] = False
    fltr[0] = fltr[1] = False
    c = 0
    for i in range(len(fltr)):
        if fltr[i]:
            c += 1
        fltr[i] = c
    plyr1 = 0
    for n in nums:
        plyr1 += fltr[n] % 2 == 1
    if plyr1 * 2 == len(nums):
        return None
    if plyr1 * 2 > len(nums):
        return playerss[0]
    return players[1]

