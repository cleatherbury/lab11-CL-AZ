"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# im here

import math
# First example
def add(a, b): 
    pass


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def exponent(a,b):
    return a ** b

def logarithm(a,b):
    return math.log(a,b)
