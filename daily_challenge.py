#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:55:42 2020

@author: Shirin
"""



def combinator(lst, sep_=""):

'''
Given a list of string lists, returns a list of all 
combinations as concatenated strings.
'''

    return [sep_.join(i) for i in product(*lst)]