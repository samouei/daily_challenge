#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updated Daily

"""
from itertools import product 
import re

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


def repeat(lst, n):
	return lst * n

def add(lst, x):
    lst.append(x)
    return lst

def remove(lst, i, j):
    del lst[i:j+1]
    return lst

def concat(lst, lst2):
    return lst + lst2

def is_ladder_safe(ldr):
    '''
    Due to a huge scandal around the Laddersons Ladder Factory creating 
    faulty ladders, the Occupational Safety and Health Administration require 
    your help in determining whether a ladder is safe enough for use in the 
    work place! It is vital that a ladder passes all criterea:

        The ladder must be at least 5 characters wide.
        The ladder mustn't have more than a 2 character gap between rungs.
        Rungs must be evenly spaced apart.
        Rungs should not be broken (i.e. no gaps).
    Given a ladder (drawn as a list of strings) return True if it passes all of OSHA's criterea.
    '''
    
    gap = ldr[0]
    rung = len(ldr[0])
    pattern = ['r' if i == rung else 'g' if i == gap else 'c' for i in ldr]
    return len(ldr[0]) > 4 and pattern == pattern[::-1] and 'ggg' not in ''.join(pattern)


def min_length(lst, n):
	res = []
	for i in range(len(lst)):
		for j in range(i + 1, len(lst) + 1):
			sublist = lst[i:j]
			if sum(sublist) > n:
				res.append(len(sublist))
	return min(res) if res else -1


def min_turns(current, target):
    '''
    Create a function that returns the smallest number of turns it takes 
    to transform the lock from the current combination to the target combination. 
    One turn is equivalent to rolling a number forwards or backwards by one.
    '''
	c = [int(i) for i in list(current)]
	t = [int(i) for i in list(target)]
	return sum([min(abs(c[i] - t[i]), 10 - abs(c[i] - t[i])) for i in range(4)])


