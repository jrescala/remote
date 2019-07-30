#!/usr/bin/env python
# -*- coding: utf-8 -*-

def double(x):
    """
    This is where you put an optional docstring that explains what the
    function does. For example, this function multiplies its input by 2.
    """
    return x * 2

def apply_to_one(f):
    """Calls the function f with 1 as its argument"""
    return f(1)

my_double = double             # refers to the previously defined function
x = apply_to_one(my_double)    # equals 2

y = apply_to_one(lambda x: x + 4)      # equals 5

print(y)

def my_print(message = "my default message"):
    print(message)

my_print(r"\thello")   # prints 'hello'
my_print()          # prints 'my default message'

def full_name(first = "What's-his-name", last = "Something"):
    return first + " " + last

print(full_name("Joel", "Grus"))     # "Joel Grus"
print(full_name("Joel"))             # "Joel Something"
print(full_name(last="Grus"))        # "What's-his-name Grus"

tab_string = "\t"       # represents the tab character
print(len(tab_string))         # is 1