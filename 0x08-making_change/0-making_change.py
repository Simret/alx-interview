#!/usr/bin/python3
'''making change'''
import sys


def makeChange(coins, total):
    '''Determining the fewest number of coins needed to meet a given
        amount total when given a pile of coins of different values'''
    if total <= 0:
        return 0
    if (coins is None or len(coins) == 0):
        return -1

    change = 0
    available_coins = sorted(coins, reverse=True)
    change_left = total

    for coin in available_coins:
        while (change_left % coin >= 0 and change_left >= coin):
            change += int(change_left / coin)
            change_left = change_left % coin

    change = change if change_left == 0 else -1

    return change
