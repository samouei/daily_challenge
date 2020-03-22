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
    
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def filter_primes(num):
    '''
    Takes a list and returns a new list containing only prime numbers.
    '''
    
    return [i for i in num if is_prime(i)]


def advanced_sort(lst):
    '''
    Takes a list of numbers or strings and returns a list 
    with the items from the original list stored into sublists. 
    Items of the same value should be in the same sublist.
    '''

    return [[i] * lst.count(i) for i in sorted(set(lst), key=lst.index)]


def shift_sentence(txt):
    '''
    Shifts the first letter of each word to the 
    next word in the sentence (shifting right).
    '''
    
    words = txt.split()
    return ' '.join(a[0] +b[1:] for a, b in zip(words[-1:] + words[:-1], words))
