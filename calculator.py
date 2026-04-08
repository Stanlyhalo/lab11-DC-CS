"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a,b): a + b
def sub(a,b): a - b
def mul(a,b): a * b
def div(a, b):
    result = 0
    try:
        if a == 0: raise ZeroDivisionError
        result = b / a
    except ZeroDivisionError:
        result = 0
    return result
def log(a, b):
    result = 0
    try:
        result = math.log(a, b)
    except ValueError:
        result = 0
    return result
def exp(a,b): a**b

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def logarithm(a, b):
    result = 0
    try:
        result = math.log(a, b)
    except ValueError:
        result = 0
    return result
def exponent(a, b): return a**b
