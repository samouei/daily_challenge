#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updated Daily

"""


from itertools import product 

def combinator(lst, sep_=""):

    '''
    Given a list of string lists, returns a list of all 
    combinations as concatenated strings.
    '''

    return [sep_.join(i) for i in product(*lst)]


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_primes(num):
    '''
    Takes a list and returns a new list containing only prime numbers.
    '''
    return [i for i in num if is_prime(i)]


<<<<<<< HEAD
=======
    return [sep_.join(i) for i in product(*lst)]
>>>>>>> b2fd7a9f39771a31d9759dfd3682e3dd2530fa9b
