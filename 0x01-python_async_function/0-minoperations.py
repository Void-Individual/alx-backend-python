#!/usr/bin/python3
"""Module containing a function for minimum operations"""


def copy_all(count, src):
    """Function to copy the entire string content and increase
    count value by 1"""
    return count + 1, src


def paste(count, src, copy):
    """Function to concatenate the last copied content and
    increment the count value by 1"""
    return count + 1, src + copy


def minOperations(n):
    """Function to determine the minimum number of operations required
    to rewrite a single letter"""

    src = 'H'
    count = 0
    copy = ''

    #count, copy = copy_all(count, src)
    #count, src = paste(count, src, copy)

    while (count < n):
        if len(src) >= n:
            print('catch')
            break
        else:
            count, copy = copy_all(count, src)
            if len(src * 2) < (n / 2):
                count, src = paste(count, src, copy)
        print(src)


    return count
