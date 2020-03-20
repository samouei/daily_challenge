#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:55:42 2020

@author: Shirin
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


