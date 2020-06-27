#!/bin/python3

import math
import os
import random
import re
import sys


#
# HackerRank problem 
#
# The Coin Change Problem
#
# You are working at the cash counter at a fun-fair, and you have different types of coins available to you in infinite
# quantities. The value of each coin is already given. Can you determine the number of ways of making change
# for a particular number of units using the given types of coins?
#
# For example, if you have  types of coins, and the value of each type is given as  respectively, you can make change
# for  units in three ways: , , and .
#
# Function Description
#
# Complete the getWays function in the editor below. It must return an integer denoting the number of ways
# to make change.
#
# getWays has the following parameter(s):
#
# n: an integer, the amount to make change for
# c: an array of integers representing available denominations


def make_change(coins, money, index, memo):
    if money == 0:
        return 1
    if index >= len(coins):
        return 0

    key = "{}-{}".format(money, index)
    if key in memo.keys():
        return memo[key]

    money_with_coins = 0
    ways = 0
    while money_with_coins <= money:
        remaining = money - money_with_coins
        ways += make_change(coins, remaining, index + 1, memo)
        money_with_coins += coins[index]
    memo.setdefault(key, ways)
    return ways


def get_ways(n, c):
    return make_change(c, n, 0, {})
