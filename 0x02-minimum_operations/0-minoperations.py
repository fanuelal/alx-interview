#!/usr/bin/python3
"""Module calculate the min num of opration"""


def minOperations(n):
    """ that calculates the fewest number of operations"""

    temp = 1
    counter = 0
    cpyall = 1
    if (n < 2):
        return 0
    if(n % 2 != 0):
        cpyall = temp
        temp = (2 * temp)
        counter += 2
        temp += cpyall
        counter += 1
    while(temp < n):
        if ((2 * temp) <= n):
            cpyall = temp
            temp = (2 * temp)
            counter += 2
        elif((temp + cpyall) <= n):
            temp = temp + cpyall
            counter += 1

    return counter
