#!/usr/bin/python3
'''
This function generates phone numbers with the specified prefix
'''
import random
import json


def new_numbers(prefix_str, total):
    ''' Prefix: e.g. 0810, 0703...
    prefix must be in string
    This is a demo: Exceptions are not handled in this code
    '''

    for i in range(0, total):
        suffix = random.randint(1001103, 9817645)
        num_str = prefix_str + str(suffix)
        with open("phone_numbers.txt", 'a') as file:
            file.write(num_str)
            file.write('\n')


# generate 50 numbers that starts with 0813
new_numbers("0813", 50)
