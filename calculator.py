"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    result = 0
    try:
        if a == 0: raise ZeroDivisionError
        result = b / a
    except ZeroDivisionError:
        result = 0
    return result
def logarithm(a, b):
    result = 0
    try:
        result = math.log(a, b)
    except ValueError:
        result = 0
    return result
def exp(a, b): return a**b
def square_root(a):
    result = 0
    try:
        if a < 0: raise ValueError
        result = math.sqrt(a)
    except ValueError:
        result = 0
    return result
def hypotenuse(a, b):
    return math.hypot(a,b)